import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from src.config import BOT_TOKEN
from src.handlers.common import employee
from src.handlers.menu.shop import sales, products, workshift
from src.handlers.menu import mainmenu


async def main():
    default = DefaultBotProperties(parse_mode='HTML')
    bot = Bot(token=BOT_TOKEN, default=default)

    dp = Dispatcher()

    dp.include_routers(
        employee.employee_router,
        mainmenu.mainmenu_router,
        sales.sales_router,
        products.products_router,
        workshift.workshift_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


