import asyncio

from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


