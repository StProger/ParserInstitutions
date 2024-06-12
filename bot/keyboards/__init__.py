from aiogram import types


def menu():

    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Информационные технологии", callback_data="s_it"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Медицина", callback_data="s_medic"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Образование (педагогика и тп.)", callback_data="s_educ"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Инженерия", callback_data="s_industry"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Международные отношения", callback_data="s_between_city"
                )
            ],
        ]
    )
