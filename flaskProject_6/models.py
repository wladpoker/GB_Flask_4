from pydantic import BaseModel

# Модель данных для таблицы "Пользователи"
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str

# Модель данных для таблицы "Заказы"
class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    status: str

# Модель данных для таблицы "Товары"
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float