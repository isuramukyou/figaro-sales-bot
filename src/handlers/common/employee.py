import base64

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.figaro.exceptions import InvalidRequest
from src.filters.is_cashier import IsCashier
from src.keyboards import reply

employee_router = Router()


@employee_router.message(CommandStart(deep_link=True))
async def cmd_deep_start(message: types.Message):
    """Диплинк /start для авторизации исключительно работников"""
    encoded_data = message.text.split()[1].replace("__", "/")
    encoded_data = encoded_data.replace("_", "+")
    decoded_data = base64.b64decode(encoded_data).decode('utf-8')
    cashier_name = decoded_data.split("_")[0]
    cashier_kassa = decoded_data.split("_")[1].replace("\r", "").replace("\n", "")

    try:
        async with FigaroAPI() as fg:
            await fg.create_cashier(cashier_name, cashier_kassa, message.from_user.id)
            await message.answer(_t.bold(f"👋 Добро пожаловать, {cashier_name}"))
    except InvalidRequest:
        return await message.answer(_t.bold("⚠️ Не удалось авторизоваться"))


    await message.answer(
        text=_t.bold('🏠 Главное меню'),
        reply_markup=reply.mainmenu_kb()
    )


@employee_router.message(CommandStart(), IsCashier())
async def cmd_start(message: types.Message):
    await message.answer(
        text=_t.bold('🏠 Главное меню'),
        reply_markup=reply.mainmenu_kb()
    )
