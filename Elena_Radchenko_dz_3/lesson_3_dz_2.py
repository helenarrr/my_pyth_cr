user_request = input("Введите числительное от 0 до 10 на английском языке прописными или строчными буквами: ")


def num_translate_adv(user_request, translator_dict):
    if user_request[0].isupper():
        user_request = user_request.lower()
        return translator_dict[user_request].capitalize()
    else:
        return translator_dict[user_request]


translator_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
    }

print(num_translate_adv(user_request, translator_dict))