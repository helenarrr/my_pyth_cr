import requests
import maya

def currency_rates_sp(arg, date=None):
    user_charcode = arg.upper()
    url_list = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.split("><")
    char_val = {}
    for el in url_list:
        if el.find("CharCode") != -1:
            charcode = el[9:12]
        elif el.find("Value") != -1:
            valute_value = float(el[6:13].replace(",", "."))
            char_val[charcode] = valute_value
        elif el.find("ValCurs Date") == 0:
            date_1 = str(el[14:24])
            date = maya.parse(date_1).datetime()
    print(char_val.get(user_charcode, None), date)