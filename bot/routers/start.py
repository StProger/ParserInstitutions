from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext

from bot.keyboards import menu

router = Router()


@router.callback_query(StateFilter("*"), F.data == "menu")
async def menu_(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()

    await callback.message.answer(text="Привет, я помогу тебе с выбором вуза в Москве. Выбери интересующую тебя специальность👇",
                                  reply_markup=menu())
    await callback.answer()
    await state.set_state("ege:spec")


@router.message(CommandStart(), StateFilter("*"))
async def start_handler(message: types.Message, state: FSMContext):

    await state.clear()

    await message.answer("Привет, я помогу тебе с выбором вуза в Москве. Выбери интересующую тебя специальность👇",
                         reply_markup=menu())
    await state.set_state("ege:spec")
