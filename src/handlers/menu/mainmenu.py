from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.figaro.exceptions import InvalidRequest

mainmenu_router = Router()


@mainmenu_router.callback_query(F.data.startswith("mainmenu"))
async def cb_mainmenu_handler(call: types.CallbackQuery):
    section = call.data.split(":")[1]
    if section == "sales":
        await call.message.answer(
            _t.bold("🏷️ Меню управления продажами"),
            reply_markup=None
        )

    elif section == "products":
        await call.message.answer(
            _t.bold("📦 Меню управления продуктами"),
            reply_markup=None
        )

    elif section == "workshift":
        await call.message.answer(
            _t.bold("💼 Ваша рабочая смена"),
            reply_markup=None
        )

        pass

