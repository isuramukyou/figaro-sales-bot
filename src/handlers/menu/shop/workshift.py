from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.utils.text_decorations import html_decoration as _t

from src.figaro.api import FigaroAPI
from src.figaro.exceptions import InvalidRequest, DataIsEmpty

workshift_router = Router()


@workshift_router.message(F.text == "👥 Кассиры на смене")
async def msg_get_cashiers(message: types.Message):
    try:
        async with FigaroAPI() as fg:
            cashiers = await fg.get_cashiers()
    except InvalidRequest:
        return await message.answer(_t.bold("⚠️ Не удалось отобразить"))
    except DataIsEmpty:
        return await message.answer(_t.bold("👥 Кассиры на смене отсутствуют"))

    cashiers_msg = _t.bold('👥 Кассиры на смене')
    for cashier in cashiers:
        cashier_msg = (f'\n\n<b>👨‍💼 Кассир: </b>{cashier["name"]}'
                       f'\n<b>💳 За кассой: </b>{cashier["kassa"]}')
        cashiers_msg += cashier_msg

    await message.answer(cashiers_msg)


@workshift_router.message(F.text == "📪 Закрыть смену")
async def msg_close_workshift(message: types.Message):
    return await message.answer("coming soon")


@workshift_router.message(F.text == "📬 Открыть смену")
async def msg_open_workshift(message: types.Message):
    return await message.answer("coming soon")
