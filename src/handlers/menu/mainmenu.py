from aiogram import Router, F, types
from aiogram.utils.text_decorations import html_decoration as _t

from src.keyboards import reply

mainmenu_router = Router()
mainmenu_router.message.filter()


@mainmenu_router.message(F.text == "Назад")
async def back2menu_handler(message: types.Message):
    await message.answer(
            text=_t.bold('🏠 Главное меню'),
            reply_markup=reply.mainmenu_kb()
        )


@mainmenu_router.message(F.text == "💼 Рабочая смена")
async def workshift_handler(message: types.Message):
    await message.answer(
            _t.bold("💼 Ваша рабочая смена"),
            reply_markup=reply.workshift_kb()
        )


@mainmenu_router.message(F.text == "🏷️ Продажи")
async def sales_handler(message: types.Message):
    await message.answer('coming soon')
    # await message.answer(
    #         _t.bold("🏷️ Меню управления продажами"),
    #         reply_markup=reply.sales_kb()
    #     )


@mainmenu_router.message(F.text == "📦 Продукты")
async def sales_handler(message: types.Message):
    await message.answer(
            _t.bold("📦 Меню управления продуктами"),
            reply_markup=reply.products_kb()
        )
