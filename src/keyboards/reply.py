from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

RKM = ReplyKeyboardMarkup
RB = KeyboardButton
RKBuilder = ReplyKeyboardBuilder


def products_kb():
    return RKM(
        keyboard=[
            [RB(text="↘️ Получить продукт")],
            [RB(text="📝 Создать продукт")]
        ], resize_keyboard=True
    )


def sales_kb():
    return RKM(
        keyboard=[
            [RB(text="↘️ Получить продукт")],
            [RB(text="📝 Создать продукт")]
        ], resize_keyboard=True
    )


def workshift_kb():
    return RKM(
        keyboard=[
            [RB(text="👥 Кассиры на смене")],
            [RB(text="📪 Закрыть смену"), RB(text="📬 Открыть смену")]
        ], resize_keyboard=True
    )
