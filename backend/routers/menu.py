from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models import MenuModel, get_db
from backend.schemas import MenuItem

router = APIRouter()


@router.get("/menu", response_model=list[MenuItem])
def get_menu(db: Session = Depends(get_db)):
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
    
    return items
