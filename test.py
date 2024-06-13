import json
import re

import requests
from bs4 import BeautifulSoup


resp = requests.get("https://moivyz.dnevnik.ru/entity/1676")
print(resp.status_code)
soup = BeautifulSoup(resp.text, "lxml")

scr = soup.find_all("script")
print(type(scr[3]))
match = re.search(r"window\.__INITIAL_STATE__ = ({.*?});", str(scr[3]))

if match:
    dictionary_string = match.group(1)
    dictionary = json.loads(dictionary_string)
    print(dictionary)
else:
    print("Словарь не найден в строке.")