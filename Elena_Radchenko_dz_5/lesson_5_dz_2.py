n = int(input("Введите число, до которого будет идти генерация нечетных чисел"))
nums_gen = (num for num in range(1, n + 1, 2))

print(*nums_gen, sep=',')
