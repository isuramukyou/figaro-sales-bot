from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

IKM = InlineKeyboardMarkup
IKB = InlineKeyboardButton
IKBuilder = InlineKeyboardBuilder


def mainmenu_kb():
    return IKM(
        inline_keyboard=[
            [IKB(text="🏷️ Продажи", callback_data="mainmenu:sales")],
            [IKB(text="📦 Продукты", callback_data="mainmenu:products")],
            [IKB(text="💼 Рабочая смена", callback_data="mainmenu:workshift")]
        ]
    )
