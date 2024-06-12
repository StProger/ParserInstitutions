from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.settings import settings
from bot.parser import parse_institutions

router = Router()


@router.callback_query(StateFilter("ege:spec"), F.data.startswith("s_"))
async def get_scores(callback: types.CallbackQuery, state: FSMContext):
    spec_dict = settings.spec_dict.copy()
    await state.update_data(
        chosen_spec=callback.data
    )
    await callback.message.answer(
        text=spec_dict[callback.data]["text"],
        parse_mode="HTML",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="Меню", callback_data="menu"
                    )
                ]
            ]
        )
    )
    await callback.answer()
    await state.set_state("ege:get_scores")


@router.message(StateFilter("ege:get_scores"))
async def get_institutions(message: types.Message, state: FSMContext):
    state_data = await state.get_data()

    spec_dict = settings.spec_dict.copy()

    subjects = []

    specialities = None

    scores = message.text.split(", ")
    # for i in range(len(scores) - 1):
    #     scores[i] = scores[i].strip()
    print(scores)

    for score in scores:

        if not score.isdigit():
            await message.answer("Введите только баллы!")
            return

    if state_data["chosen_spec"] == "s_between_city":

        if len(scores) != 4:
            await message.answer("Введите баллы за все предметы.")
            return

        if int(scores[0]) < spec_dict["s_between_city"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])
        if int(scores[1]) < spec_dict["s_between_city"]["min_communic"]:
            await message.answer("Минимальный балл за обществознание: 45")
            return
        subjects.append(settings.sub_dict["communic"])

        if int(scores[2]) != 0:

            if int(scores[2]) < spec_dict["s_between_city"]["min_inyz"]:
                await message.answer("Минимальный балл за английский язык: 30")
                return
            subjects.append(settings.sub_dict["inyz"])

        if int(scores[3]) != 0:

            if int(scores[3]) < spec_dict["s_between_city"]["min_history"]:
                await message.answer("Минимальный балл за английский язык: 35")
                return
            subjects.append(settings.sub_dict["history"])

        specialities = spec_dict["s_between_city"]["specialities"]

    elif state_data["chosen_spec"] == "s_it":

        if int(scores[0]) < spec_dict["s_it"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])
        if int(scores[1]) < spec_dict["s_it"]["min_math"]:
            await message.answer("Минимальный балл за математику: 39")
            return
        subjects.append(settings.sub_dict["math"])

        if int(scores[2]) < spec_dict["s_it"]["min_inf"]:
            await message.answer("Минимальный балл за информатику: 44")
            return
        subjects.append(settings.sub_dict["inf"])

        specialities = spec_dict["s_it"]["specialities"]


    elif state_data["chosen_spec"] == "s_medic":

        if int(scores[0]) < spec_dict["s_it"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])

        if int(scores[1]) < spec_dict["s_medic"]["min_bio"]:
            await message.answer("Минимальный балл за биологию: 39")
            return
        subjects.append(settings.sub_dict["bio"])

        if int(scores[2]) < spec_dict["s_medic"]["min_chem"]:
            await message.answer("Минимальный балл за химию: 39")
            return
        subjects.append(settings.sub_dict["chemistry"])

        specialities = spec_dict["s_medic"]["specialities"]

    elif state_data["chosen_spec"] == "s_educ":

        if int(scores[0]) < spec_dict["s_educ"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])

        if int(scores[1]) < spec_dict["s_educ"]["min_communic"]:
            await message.answer("Минимальный балл за обществознание: 45")
            return
        subjects.append(settings.sub_dict["communic"])

        if int(scores[2]) < spec_dict["s_educ"]["min_history"]:
            await message.answer("Минимальный балл за историю: 35")
            return
        subjects.append(settings.sub_dict["history"])

        specialities = spec_dict["s_educ"]["specialities"]

    elif state_data["chosen_spec"] == "s_industry":

        if int(scores[0]) < spec_dict["s_industry"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return

        subjects.append(settings.sub_dict["russia"])

        if int(scores[1]) < spec_dict["s_industry"]["min_math"]:
            await message.answer("Минимальный балл за математику: 39")
            return
        subjects.append(settings.sub_dict["math"])

        if int(scores[2]) < spec_dict["s_industry"]["min_physics"]:
            await message.answer("Минимальный балл за физику: 39")
            return
        subjects.append(settings.sub_dict["physician"])

        specialities = spec_dict["s_industry"]["specialities"]

    request_body = {
        'cities': [3],
        'professions': [],
        'educationForms': [],
        'specialities': specialities,
        'subjects': subjects,
        'spoTypes': [],
        'spoEducationalBases': [],
        'paid': True,
        'free': True,
        'hasDorm': False,
        'hasMilDep': False,
        'spoVuzRel': None,
        'stateInstitution': None,
        'searchSpo': False,
        'limit': 15,
        'score': sum(list(map(int, scores))),
        'employers': [],
    }
    data = parse_institutions(request_body)
    print(data)

    text = ""

    for index, inst in enumerate(data["institutions"]):
        if index > 2:
            break
        text += (f"<b>{inst['name']}</b>\n"
                 f"Бюджетных мест: {inst.get('freePlaces', "нет")}\n"
                 f"Платных мест: {inst.get('paidPlaces', 'нет')}\n"
                 f"Минимальный балл на бюджет: {inst.get('minFreePassScore', '<b>-</b>')}\n"
                 f"Минимальный балл платно: {inst.get('minPaidPassScore', '<b>-</b>')}\n"
                 f"Минимальная стоимость на платную основу: {inst.get('minPrice', '<b>-</b>')}\n")

        if inst.get('site'):

            text += f"Сайт: <a href='{inst.get('site')}'>{inst.get('shortName', 'ссылка')}</a>\n"

        text += "➖➖➖➖➖➖➖➖➖➖➖➖\n"


    await message.answer(
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )


