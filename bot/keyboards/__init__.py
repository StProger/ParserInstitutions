from aiogram import types


def menu():

    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Информационная безопасность", callback_data="s_it"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Стоматология", callback_data="s_medic"
                )
            ],
            # [
            #     types.InlineKeyboardButton(
            #         text="Педагог", callback_data="s_educ"
            #     )
            # ],
            [
                types.InlineKeyboardButton(
                    text="Строительство", callback_data="s_industry"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Международные отношения", callback_data="s_between_city"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Социология", callback_data="s_sociology"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Юрист", callback_data="s_urist"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Философия", callback_data="s_philo"
                )
            ]
        ]
    )
