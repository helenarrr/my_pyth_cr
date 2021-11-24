user_percent = int(input("Введите проценты: "))

if (user_percent == 1) or (user_percent % 10 == 1 and user_percent > 11):
    value = "Процент"
elif (user_percent <= 4) or (2 <= user_percent % 10 <= 4 and user_percent > 14):
    value = "Процента"
else:
    value = "Процентов"

print(user_percent, value)