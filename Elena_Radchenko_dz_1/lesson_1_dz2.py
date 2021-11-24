my_list_number = []
for i in range(1, 1001, 2):
    my_list_number.append(i ** 3)

final_sum_1 = 0
for num in my_list_number:
    sum_check = 0
    for num_check in str(num):
        sum_check += int(num_check)
    if sum_check % 7 == 0:
        final_sum_1 += num
print(final_sum_1)

final_sum_2 = 0
for num in my_list_number:
    num += 17
    sum_check = 0
    for num_check in str(num):
        sum_check += int(num_check)
    if sum_check % 7 == 0:
        final_sum_2 += num
print(final_sum_2)