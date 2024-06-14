from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

from bot.settings import settings
from bot.parser import parse_institutions, get_url_map, parser_current_vuz

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

    chose_spec = ""

    scores = message.text.split(",")
    # print(scores)
    for i in range(len(scores)):
        scores[i] = scores[i].strip()
    # print(scores)

    for score in scores:

        if not score.isdigit():
            await message.answer("Введите только баллы!")
            return

    if state_data["chosen_spec"] == "s_between_city":

        if len(scores) != 4:
            await message.answer("Введите баллы за все предметы.")
            return

        chose_spec = "Международные отношения"

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
        chose_spec = "Информационная безопасность"
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
        chose_spec = "Стоматология"
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
        chose_spec = "Педагог"
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

        chose_spec = "Строительство"

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

    elif state_data["chosen_spec"] == "s_sociology":

        if len(scores) != 4:
            await message.answer("Введите баллы за все предметы.")
            return

        chose_spec = "Социология"

        if int(scores[0]) < spec_dict["s_sociology"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])
        if int(scores[1]) < spec_dict["s_sociology"]["min_communic"]:
            await message.answer("Минимальный балл за обществознание: 45")
            return
        subjects.append(settings.sub_dict["communic"])

        if int(scores[2]) != 0:

            if int(scores[2]) < spec_dict["s_sociology"]["min_inyz"]:
                await message.answer("Минимальный балл за английский язык: 30")
                return
            subjects.append(settings.sub_dict["inyz"])

        if int(scores[3]) != 0:

            if int(scores[3]) < spec_dict["s_sociology"]["min_history"]:
                await message.answer("Минимальный балл за английский язык: 35")
                return
            subjects.append(settings.sub_dict["history"])

        specialities = spec_dict["s_sociology"]["specialities"]

    elif state_data["chosen_spec"] == "s_urist":

        if len(scores) != 4:
            await message.answer("Введите баллы за все предметы.")
            return

        chose_spec = "Юриспруденция"

        if int(scores[0]) < spec_dict["s_urist"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return
        subjects.append(settings.sub_dict["russia"])
        if int(scores[1]) < spec_dict["s_urist"]["min_communic"]:
            await message.answer("Минимальный балл за обществознание: 45")
            return
        subjects.append(settings.sub_dict["communic"])

        if int(scores[2]) != 0:

            if int(scores[2]) < spec_dict["s_urist"]["min_inyz"]:
                await message.answer("Минимальный балл за английский язык: 30")
                return
            subjects.append(settings.sub_dict["inyz"])

        if int(scores[3]) != 0:

            if int(scores[3]) < spec_dict["s_urist"]["min_history"]:
                await message.answer("Минимальный балл за английский язык: 35")
                return
            subjects.append(settings.sub_dict["history"])

        specialities = spec_dict["s_urist"]["specialities"]

    elif state_data["chosen_spec"] == "s_philo":

        if int(scores[0]) < spec_dict["s_philo"]["min_rus"]:
            await message.answer("Минимальный балл за русский язык: 40")
            return

        chose_spec = "Философия"

        subjects.append(settings.sub_dict["russia"])
        if int(scores[1]) < spec_dict["s_philo"]["min_communic"]:
            await message.answer("Минимальный балл за обществознание: 45")
            return
        subjects.append(settings.sub_dict["communic"])

        if int(scores[2]) < spec_dict["s_philo"]["min_history"]:
            await message.answer("Минимальный балл за английский язык: 35")
            return
        subjects.append(settings.sub_dict["history"])

        specialities = spec_dict["s_philo"]["specialities"]


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
    # print(data)

    text = "Вот какие университеты могу вам предложить по вашим баллам👇\n\n"
    count = 0
    builder = InlineKeyboardBuilder()
    for index, inst in enumerate(data["institutions"]):
        if count > 2:
            break

        desc_vuz = parser_current_vuz(vuz_id=inst["id"], spec=specialities)

        if desc_vuz == "ERROR":
            await message.answer("Произошла ошибка.")
            return

        if desc_vuz is None:
            continue

        address = inst.get("address")

        map_ = None

        if address is not None:
            map_ = get_url_map(f"Москва, {address}")

        name = inst["name"]
        short_name = inst["shortName"]

        site = inst["site"]

        price = desc_vuz[0].get("price")

        if price is None:

            price = "Нет"

        free_places = desc_vuz[0].get("freePlaces")

        if free_places is None:
            free_places = "нет"

        paid_places = desc_vuz[0].get("paidPlaces")

        if paid_places is None:

            paid_places = "нет"

        free_ege_pass_score = desc_vuz[0].get("freeEgePassScore")

        if free_ege_pass_score is None or free_ege_pass_score == 0.0:

            free_ege_pass_score = "<b>-</b>"

        paid_ege_pass_score = desc_vuz[0].get("paidEgePassScore")

        if paid_ege_pass_score is None or paid_ege_pass_score == 0.0:

            paid_ege_pass_score = "<b>-</b>"

        text += (f"<b>{name}</b>\n"
                 f"Бюджетных мест: {free_places}\n"
                 f"Платных мест: {paid_places}\n"
                 f"Минимальный балл на бюджет: {int(free_ege_pass_score) if type(free_ege_pass_score) != str else free_ege_pass_score}\n"
                 f"Минимальный балл платно: {int(paid_ege_pass_score) if type(paid_ege_pass_score) != str else paid_ege_pass_score}\n"
                 f"Стоимость на платную основу: {price}\n")
        if address:
            text += f"Адрес: <code>{address}</code>\n"

        if site:

            text += f"Сайт: <a href='{site}'>{short_name}</a>\n"

        # if map_:
        #
        #     builder.row(
        #         InlineKeyboardButton(
        #             text=short_name, url=map_
        #         )
        #     )

        text += "➖➖➖➖➖➖➖➖➖➖➖➖\n"
        count += 1

    await message.answer(
        text=f"Спасибо! Ваш балл равен: {sum(list(map(int, scores)))}"
    )

    await message.answer(
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await message.answer(
        text="Для возвращения в меню напишите /start"
    )

