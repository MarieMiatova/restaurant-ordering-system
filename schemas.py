from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# API Contract - схемы для меню и заказов

class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    image: Optional[str] = None


class OrderCreate(BaseModel):
    items: List[dict]
    customer_name: str
    customer_phone: str


class OrderStatusUpdate(BaseModel):
    status: str


class Order(BaseModel):
    id: int
    items: List[dict]
    customer_name: str
    customer_phone: str
    status: str
    created_at: datetime
