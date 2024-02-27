from pydantic import BaseModel, Field


class FigaroProduct(BaseModel):
    name: str = Field(description='Наименование продукта')
    weight: int = Field(description='Вес продукта')
    size: str = Field(description='Размер продукта')


class Cashier(BaseModel):
    name: str
    kassa: str
    ID: str


class ChequeProducts(BaseModel):
    product: str
    amount: str
    price: str
    discount: str
    total: str
    costPrice: str
    myProfit: str


class FigaroCheque(BaseModel):
    totalAmount: str = Field()
    profit: str = Field()
    comment: str = Field()
    cashier: str = Field()
    store: str
    sourceSales: str
    paymentMethod: str
    gender: str
    products: list[ChequeProducts]
