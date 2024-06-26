from pydantic import BaseModel
from decimal import Decimal


class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    is_verified: bool

    @classmethod
    def create(cls, data: dict) -> "Customer":
        return cls(
            id=data.get("customer_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            is_verified=data.get("is_verified"),
        )


class OrderItem(BaseModel):
    id: int
    name: str
    price: Decimal
    count: int

    @classmethod
    def create(cls, data: dict) -> "OrderItem":
        return cls(
            id=data.get("order_item_id"),
            name=data.get("name"),
            price=data.get("price"),
            count=data.get("count"),
        )


class Order(BaseModel):
    id: int
    status: int
    customer: Customer
    items: list[OrderItem]

    @classmethod
    def create(cls, data: dict) -> "Order":
        return cls(
            id=data.get("order_id"),
            status=data.get("status"),
            customer=Customer.create(data=data.get("customer")),
            items=[OrderItem.create(data=item) for item in data.get("items")],
        )
