from fastapi import FastAPI, HTTPException
from schemas import MenuItem, OrderCreate, Order, OrderItem
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/restaurant_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class MenuModel(Base):
    __tablename__ = "menu"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    image = Column(String, nullable=True)


class OrderModel(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    phone = Column(String)
    address = Column(String)
    total_amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.now)


class OrderItemModel(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer)
    quantity = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/menu")
def get_menu():
    db = SessionLocal()
    try:
        items = db.query(MenuModel).all()
        
        if len(items) == 0:
            default_items = [
                MenuModel(name="Пицца Маргарита", description="Сыр, томаты, базилик", price=450.0, category="Пицца", image="https://example.com/margarita.jpg"),
                MenuModel(name="Пицца Пепперони", description="Пепперони, сыр, томатный соус", price=550.0, category="Пицца", image="https://example.com/pepperoni.jpg"),
                MenuModel(name="Борщ", description="Традиционный украинский борщ со сметаной", price=320.0, category="Супы", image="https://example.com/borscht.jpg"),
                MenuModel(name="Цезарь с курицей", description="Салат с курицей, пармезаном и сухариками", price=380.0, category="Салаты", image="https://example.com/caesar.jpg"),
                MenuModel(name="Паста Карбонара", description="Спагетти с беконом, яйцом и пармезаном", price=420.0, category="Паста", image="https://example.com/carbonara.jpg"),
                MenuModel(name="Тирамису", description="Классический итальянский десерт", price=290.0, category="Десерты", image="https://example.com/tiramisu.jpg"),
                MenuModel(name="Чизкейк", description="Нежный творожный чизкейк", price=310.0, category="Десерты", image="https://example.com/cheesecake.jpg"),
                MenuModel(name="Лимонад домашний", description="Освежающий лимонад с мятой", price=150.0, category="Напитки", image="https://example.com/lemonade.jpg"),
            ]
            
            for item in default_items:
                db.add(item)
            db.commit()
            
            items = db.query(MenuModel).all()
        
        result = []
        for item in items:
            result.append({
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "category": item.category,
                "image": item.image
            })
        return result
    finally:
        db.close()


@app.post("/api/orders", response_model=Order)
def create_order(order: OrderCreate):
    db = SessionLocal()
    try:
        total = 0.0
        for item in order.items:
            menu_item = db.query(MenuModel).filter(MenuModel.id == item.menu_item_id).first()
            
            if menu_item is None:
                raise HTTPException(status_code=400, detail=f"Menu item with id {item.menu_item_id} not found")
            
            total += menu_item.price * item.quantity
        
        new_order = OrderModel(
            customer_name=order.customer_name,
            phone=order.phone,
            address=order.address,
            total_amount=total,
            status="pending",
            created_at=datetime.now()
        )
        
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        
        for item in order.items:
            order_item = OrderItemModel(
                order_id=new_order.id,
                menu_item_id=item.menu_item_id,
                quantity=item.quantity
            )
            db.add(order_item)
        
        db.commit()
        
        order_items = []
        for item in order.items:
            order_items.append(OrderItem(menu_item_id=item.menu_item_id, quantity=item.quantity))
        
        return Order(
            id=new_order.id,
            customer_name=new_order.customer_name,
            phone=new_order.phone,
            address=new_order.address,
            items=order_items,
            total_amount=new_order.total_amount,
            status=new_order.status,
            created_at=new_order.created_at
        )
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
