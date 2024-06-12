from bot.settings import settings

from aiogram import Dispatcher, Bot

from bot.routers import register_all_routers

import asyncio

import logging


async def main():

    dp = Dispatcher()
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    register_all_routers(dp)
    try:

        await dp.start_polling(bot)
    except:

        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())