from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.figaro.exceptions import InvalidRequest
from src.keyboards import reply

mainmenu_router = Router()



@mainmenu_router.message(F.text == "💼 Рабочая смена")
async def workshift_handler(message: types.Message):
    await message.answer(
            _t.bold("💼 Ваша рабочая смена"),
            reply_markup=reply.workshift_kb()
        )


@mainmenu_router.message(F.text == "🏷️ Продажи")
async def sales_handler(message: types.Message):
    await message.answer(
            _t.bold("🏷️ Меню управления продажами"),
            reply_markup=reply.sales_kb()
        )


@mainmenu_router.message(F.text == "📦 Продукты")
async def sales_handler(message: types.Message):
    await message.answer(
            _t.bold("📦 Меню управления продуктами"),
            reply_markup=reply.products_kb()
        )
