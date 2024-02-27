from aiogram import Router, F, types
from aiogram.filters import StateFilter, CommandStart
from aiogram.utils.text_decorations import html_decoration as _t

from src.keyboards import inline

employee_router = Router()


@employee_router.message(CommandStart(deep_link=True, magic=F.args == "fg"))
async def cmd_deep_start(message: types.Message):
    """Диплинк start=fg для авторизации исключительно работников"""
    await message.answer(
        text=_t.bold('👋 Добро пожаловать'),
        reply_markup=inline.mainmenu_kb()
    )
