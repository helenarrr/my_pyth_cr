user_request = input("Введите числительное от 0 до 10 на английском языке: ")


def num_translate(user_request, translator_dict):
    return translator_dict.get(user_request)


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

print(num_translate(user_request, translator_dict))