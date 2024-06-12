from aiogram import Dispatcher

from bot.routers import start, get_inst


def register_all_routers(dp: Dispatcher):

    dp.include_router(start.router)
    dp.include_router(get_inst.router)
