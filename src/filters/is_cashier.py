from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.figaro.api import FigaroAPI


class IsCashier(BaseFilter):
    async def __call__(self, message: Message):
        async with FigaroAPI() as fg:
            cashiers = await fg.get_cashiers()
        for cashier in cashiers:
            if cashier["ID"] == str(message.from_user.id):
                return True
        return False
