import json

import aiohttp

from ..config import API_PASSWORD, API_USERNAME, API_HOST
from ..figaro.exceptions import InvalidRequest, DataIsEmpty
from ..figaro.base import FigaroAPIMethods, Figaro
from ..figaro.models import FigaroProduct


class FigaroAPI(Figaro):
    def __init__(self):
        self._host = API_HOST
        self._username = API_USERNAME
        self._password = API_PASSWORD
        self.methods = FigaroAPIMethods

    async def __aenter__(self):
        # шедевросервачок без сертификатов
        connector = aiohttp.TCPConnector(ssl=False)
        self._session = aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(self._username, self._password),
            connector=connector
        )
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    async def get_all_sales(self) -> dict:
        async with self._session.get(
            url=self._host + self.methods.all_sales
        ) as response:
            if response.status != 200:
                raise InvalidRequest
            return await self._json(await response.read())


    async def get_one_sale(self, product_code: str) -> dict:
        async with self._session.get(
            url=self._host + self.methods.one_sale.format(product_code)
        ) as response:
            if response.status != 200:
                raise InvalidRequest
            return await self._json(await response.read())

    async def create_cheque(self) -> dict:  # TODO
        async with self._session.post(
            url=self._host + self.methods.chek
        ) as response:
            if response.status != 200:
                raise InvalidRequest
            return await self._json(await response.read())

    async def get_product(self, product_code: str) -> dict:
        async with self._session.get(
            url=self._host + self.methods.get_product.format(product_code)
        ) as response:
            if response.status != 200:
                raise InvalidRequest
            product = await self._json(await response.read())
            if not product:
                raise DataIsEmpty
            return product

    async def create_product(self, product_name: str, product_weight: str, product_size: str) -> None:
        product = FigaroProduct(name=product_name, weight=product_weight, size=product_size)
        req_raw = product.model_dump()
        async with self._session.post(
            url=self._host + self.methods.create_product,
            json=req_raw
        ) as response:
            if response.status != 200:
                raise InvalidRequest

    async def get_cashiers(self) -> list:
        async with self._session.get(
            url=self._host + self.methods.get_cashiers
        ) as response:
            if response.status != 200:
                raise InvalidRequest
            cashiers = await self._json(await response.read())
            if not cashiers:
                raise DataIsEmpty
            return cashiers


    @staticmethod
    async def _json(data):
        return json.loads(data)


