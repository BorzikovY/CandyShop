from enum import Enum

import strawberry


@strawberry.type
class Candy:
    id: int
    name: str
    price: float
    category_id: int
    description: str
    in_stock: bool


@strawberry.type
class Category:
    id: int
    name: str
    description: str


@strawberry.enum
class OrderStatus(Enum):
    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


@strawberry.type
class OrderItem:
    candy_id: int
    quantity: int


@strawberry.type
class Order:
    id: int
    items: list[OrderItem]
    status: OrderStatus
    created_at: str
    total: float
