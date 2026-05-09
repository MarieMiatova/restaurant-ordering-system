from fastapi import FastAPI
from schemas import MenuItem

app = FastAPI()


# Моковые данные для меню
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


@app.get("/api/menu")
def get_menu():
    return menu_data
