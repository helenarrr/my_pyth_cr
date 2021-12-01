import requests


def currency_rates(arg):
    user_charcode = arg.upper()
    url_list = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.split("><")
    char_val = {}
    for el in url_list:
        if el.find("CharCode") != -1:
            charcode = el[9:12]
        elif el.find("Value") != -1:
            valute_value = float(el[6:13].replace(",", "."))
            char_val[charcode] = valute_value
    print(char_val.get(user_charcode, None))


currency_rates("hgk")
currency_rates("usd")
currency_rates("eur")
