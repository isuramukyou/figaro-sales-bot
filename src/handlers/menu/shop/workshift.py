from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.figaro.exceptions import InvalidRequest

other_router = Router()


@other_router.message(F.text == "👨‍💼 Кассиры")
async def get_cashiers(message: types.Message):
    try:
        async with FigaroAPI() as fg:
            cashiers = await fg.get_cashier()
    except InvalidRequest:
        return await message.answer(_t.bold("⚠️ Не удалось"))
        pass
