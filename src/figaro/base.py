from abc import ABC, abstractmethod


class FigaroAPIMethods:
    all_sales: str = 'Sales/all'
    one_sale: str = 'Sales/One/{}'
    chek: str = 'Sales/chek'

    get_product: str = 'products/get_product/{}'
    create_product: str = 'products/create_product'

    get_cashier: str = 'other/cashier'


class Figaro(ABC):
    # ++sales
    @abstractmethod
    async def get_all_sales(self) -> list[dict]:
        """
        Метод для получения всех продаж.
        GET: Sales/all
        """
        pass

    @abstractmethod
    async def get_one_sale(self, product_code: str) -> dict:
        """
        Метод для получения указанного продукта по его коду.
        GET: Sales/One/{product_code}
        Args:
            product_code (str): Код продукта
        """

    @abstractmethod
    async def create_cheque(self) -> dict:  # TODO
        """
        Метод для создания чека.
        POST: Sales/chek
        Args: ...
        Raw: ...
        :return:
        """

    # --sales

    # ++products
    @abstractmethod
    async def get_product(self, product_code: str) -> dict:
        """
        Метод для получения инфо указанного продукта.
        GET: products/get_product/{product_code}
        Args:
            product_code (str): Код продукта
        """

    @abstractmethod
    async def create_product(self, product_name: str, product_weight: str, product_size: str) -> None:
        """
        Метод для создания продукта по его данным.
        POST: products/create_product
        Raw:
        {"name": product_name,"weight": product_weight,"size": product_size}
        Args:
        """

    # --products

    # ++other
    @abstractmethod  # NEW
    async def get_cashier(self) -> dict:
        """
        Метод для получения инфо о кассире.
        GET: other/cashier
        """
    # --other
