from abc import ABC, abstractmethod


class FigaroAPIMethods:
    all_sales: str = 'sales/all'
    one_sale: str = 'sales/one/{}'
    chek: str = 'sales/chek'

    get_product: str = 'products/getProduct/{}'
    create_product: str = 'products/createProduct'

    get_cashiers: str = 'other/cashiers'
    create_cashier: str = 'other/createCashier'


class Figaro(ABC):
    # ++sales
    @abstractmethod
    async def get_all_sales(self) -> list[dict]:
        """
        Метод для получения всех продаж.
        GET: sales/all
        """
        pass

    @abstractmethod
    async def get_one_sale(self, product_code: str) -> dict:
        """
        Метод для получения указанного продукта по его коду.
        GET: sales/one/{product_code}
        Args:
            product_code (str): Код продукта
        """

    @abstractmethod
    async def create_cheque(self) -> dict:  # TODO
        """
        Метод для создания чека.
        POST: sales/chek
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
        GET: products/getProduct/{product_code}
        Args:
            product_code (str): Код продукта
        """

    @abstractmethod
    async def create_product(self, product_name: str, product_weight: str, product_size: str) -> None:
        """
        Метод для создания продукта по его данным.
        POST: products/createProduct
        Raw:
        {"name": product_name,"weight": product_weight,"size": product_size}
        Args:
        """

    # --products

    # ++other
    @abstractmethod  # NEW
    async def get_cashiers(self) -> list:
        """
        Метод для получения всех кассиров.
        GET: other/cashiers
        """

    @abstractmethod
    async def create_cashier(self, name: str, kassa: str, user_id: int):
        """
        Метод для авторизации кассира
        POST: other/createCashier
        """
        pass
    # --other
