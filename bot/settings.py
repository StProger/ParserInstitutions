from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

import os

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):


    BOT_TOKEN: str = os.getenv("BOT_TOKEN")


    spec_dict: dict = {
        "s_it": {
            "text": "Введите баллы за Русский язык, Математику (профиль), Информатику в формате <code>60, 60, 60</code>"
                    " соответственно.",
            "min_rus": 40,
            "min_math": 39,
            "min_inf": 44,
            "specialities": [
                "Информационная безопасность"
            ]
        },
        "s_medic": {
            "text": "Введите баллы за Русский язык, Биологию, Химию в формате <code>60, 60, 60</code>"
                    " соответственно.",
            "min_rus": 40,
            "min_bio": 39,
            "min_chem": 39,
            "specialities": [
                "Стоматология"
            ]
        },
        "s_educ": {
            "text": "Введите баллы за Русский язык, Обществознание, Историю в формате <code>60, 60, 60</code>"
                    " соответственно.",
            "min_rus": 40,
            "min_communic": 45,
            "min_history": 35,
            "specialities": [
                "Педагогическое образование"
            ]
        },
        "s_industry": {
            "text": "Введите баллы за Русский язык, Математику (профиль), Физику в формате <code>60, 60, 60</code>"
                    " соответственно.",
            "min_rus": 40,
            "min_math": 39,
            "min_physics": 39,
            "specialities": [
                "Строительство"
            ]
        },
        "s_between_city": {
            "text": "Введите баллы за Русский язык, Обществознание, Английский язык/История в формате <code>60, 60, 60, 60</code>"
                    " соответственно. <b>Если вы сдавали только английский или историю, то напишите 0 на соотвествующий предмет.</b>",
            "min_rus": 40,
            "min_communic": 45,
            "min_inyz": 30,
            "min_history": 35,
            "specialities": [
                "Международные отношения"
            ]
        },
        "s_sociology": {
            "text": "Введите баллы за Русский язык, Обществознание, Английский язык/История в формате <code>60, 60, 60, 60</code>"
                    " соответственно. <b>Если вы сдавали только английский или историю, то напишите 0 на соотвествующий предмет.</b>",
            "min_rus": 40,
            "min_communic": 45,
            "min_inyz": 30,
            "min_history": 35,
            "specialities": [
                "Социология"
            ]
        },
        "s_urist": {
            "text": "Введите баллы за Русский язык, Обществознание, Английский язык/История в формате <code>60, 60, 60, 60</code>"
                    " соответственно. <b>Если вы сдавали только английский или историю, то напишите 0 на соотвествующий предмет.</b>",
            "min_rus": 40,
            "min_communic": 45,
            "min_inyz": 30,
            "min_history": 35,
            "specialities": [
                "Юриспруденция"
            ]
        },
        "s_urist": {
            "text": "Введите баллы за Русский язык, Обществознание, Историю в формате <code>60, 60, 60</code>"
                    " соответственно. <b>Если вы сдавали только английский или историю, то напишите 0 на соотвествующий предмет.</b>",
            "min_rus": 40,
            "min_communic": 45,
            "min_inyz": 30,
            "min_history": 35,
            "specialities": [
                "Философия"
            ]
        },
    }

    sub_dict: dict = {
        "bio": "10",
        "inyz": "6",
        "geo": "9",
        "inf": "7",
        "history": "5",
        "liter": "1",
        "math": "4",
        "communic": "3",
        "russia": "2",
        "physician": "8",
        "chemistry": "11"
    }


    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
