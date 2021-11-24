duration = int(input("Введите продолжительность времени, в секундах: "))

days = duration // 86400 % 24
hours = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60
print(f"Продолжительность времени равна: {days}дней, {hours}часов, {minutes}минут, {seconds}секунд")