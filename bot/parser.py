import json
import re

import requests
from bs4 import BeautifulSoup


def parse_institutions(request_body):

    headers = {
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'tmr_lvid=0cb036881e1cb88af9e6ba58ca345678; tmr_lvidTS=1718178126088; dnevnik_sst=db310c78-90b8-4f5d-8e3b-7944007a152a%7C13.06.2024%2007%3A42%3A08; _ym_uid=1718178127430567700; _ym_d=1718178127; _ym_isad=1; domain_sid=lugsgriIplF7lB6CDCI3v%3A1718178127620; tmr_detect=1%7C1718181776500; _ym_visorc=w',
        'Origin': 'https://moivyz.dnevnik.ru',
        'Referer': 'https://moivyz.dnevnik.ru/choose',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'accept': 'application/json',
        'content-type': 'application/json',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-requested-with': 'XMLHttpRequest',
    }

    url = 'https://moivyz.dnevnik.ru/api/institutions/search'
    resp = requests.post(url, json=request_body, headers=headers)

    return resp.json()


def parser_current_vuz(vuz_id: int, spec: list):

    resp = requests.get(f"https://moivyz.dnevnik.ru/entity/{vuz_id}")
    # print(resp.status_code)
    soup = BeautifulSoup(resp.text, "lxml")

    scr = soup.find_all("script")

    match = re.search(r"window\.__INITIAL_STATE__ = ({.*?});", str(scr[3]))

    if match:
        dictionary_string = match.group(1)
        dictionary = json.loads(dictionary_string)
        current_spec = list(filter(lambda spec_: spec_["name"] in spec, dictionary["entityData"]["programs"]))
        # print(current_spec)
        if len(current_spec) == 0:
            return None
        return current_spec
    else:
        print("Словарь не найден в строке.")
        return "ERROR"

def get_url_map(address: str):

    return f"https://yandex.ru/maps/?text={address}"
