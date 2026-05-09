from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    image: Optional[str] = None


class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int


class OrderCreate(BaseModel):
    customer_name: str
    phone: str
    address: str
    items: List[OrderItem]


class OrderStatusUpdate(BaseModel):
    status: str


class Order(BaseModel):
    id: int
    customer_name: str
    phone: str
    address: str
    items: List[OrderItem]
    total_amount: float
    status: str
    created_at: datetime
