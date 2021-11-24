#1
price_list = [68.9, 90.6, 10.45, 49.3, 89, 12.70, 45.12, 56.89, 34.96, 65.10, 100, 67.02]

for price in price_list:
    rubl = int(price)
    cop = (price - rubl) * 100
    print(f"{rubl} рублей и {cop:02.0f} копеек")
#2
price_list = [68.9, 90.6, 10.45, 49.3, 89, 12.70, 45.12, 56.89, 34.96, 65.10, 100, 67.02]
print(id(price_list))
price_list.sort()
print(id(price_list))

for price in price_list:
    rubl = int(price)
    cop = (price - rubl) * 100
    print(f"{rubl} рублей и {cop:02.0f} копеек")

#3
price_list = [68.9, 90.6, 10.45, 49.3, 89, 12.70, 45.12, 56.89, 34.96, 65.10, 100, 67.02]
print(price_list)
rev_price_list = price_list[::-1]
rev_price_list.sort(reverse=True)
print(rev_price_list)
for price in rev_price_list:
    rubl = int(price)
    cop = (price - rubl) * 100
    print(f"{rubl} рублей и {cop:02.0f} копеек")
#4
for price in rev_price_list[::-1][:5]:
        rubl = int(price)
        cop = (price - rubl) * 100
        print(f"{rubl} рублей и {cop:02.0f} копеек")