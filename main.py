from fastapi import FastAPI, HTTPException
from schemas import MenuItem, OrderCreate, Order, OrderItem
from datetime import datetime

app = FastAPI()


menu_data = [
    {
        "id": 1,
        "name": "Пицца Маргарита",
        "description": "Сыр, томаты, базилик",
        "price": 450.0,
        "category": "Пицца",
        "image": "https://example.com/margarita.jpg"
    },
    {
        "id": 2,
        "name": "Борщ",
        "description": "Традиционный украинский суп со свеклой",
        "price": 320.0,
        "category": "Супы",
        "image": "https://example.com/borscht.jpg"
    },
    {
        "id": 3,
        "name": "Цезарь с курицей",
        "description": "Салат с курицей, пармезаном и сухариками",
        "price": 380.0,
        "category": "Салаты",
        "image": "https://example.com/caesar.jpg"
    }
]

orders_db = []
order_counter = 0


@app.get("/api/menu")
def get_menu():
    return menu_data


@app.post("/api/orders", response_model=Order)
def create_order(order: OrderCreate):
    global order_counter
    
    total = 0.0
    for item in order.items:
        menu_item = None
        for m in menu_data:
            if m["id"] == item.menu_item_id:
                menu_item = m
                break
        
        if menu_item is None:
            raise HTTPException(status_code=400, detail=f"Menu item with id {item.menu_item_id} not found")
        
        total += menu_item["price"] * item.quantity
    
    order_counter += 1
    
    new_order = Order(
        id=order_counter,
        customer_name=order.customer_name,
        phone=order.phone,
        address=order.address,
        items=order.items,
        total_amount=total,
        status="pending",
        created_at=datetime.now()
    )
    
    orders_db.append(new_order)
    
    return new_order
