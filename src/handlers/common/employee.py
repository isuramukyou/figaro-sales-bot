from aiogram import Router, F, types
from aiogram.filters import StateFilter, CommandStart, Command
from aiogram.utils.text_decorations import html_decoration as _t

from src.keyboards import reply
from src.filters.is_cashier import IsCashier


employee_router = Router()
employee_router.message.filter(IsCashier())


@employee_router.message(CommandStart(deep_link=True, magic=F.args == "fg"))
async def cmd_deep_start(message: types.Message):
    """Диплинк start=fg для авторизации исключительно работников"""
    await message.answer(
        text=_t.bold('👋 Добро пожаловать'),
        reply_markup=reply.mainmenu_kb()
    )


@employee_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        text=_t.bold('👋 Добро пожаловать'),
        reply_markup=reply.mainmenu_kb()
    )
