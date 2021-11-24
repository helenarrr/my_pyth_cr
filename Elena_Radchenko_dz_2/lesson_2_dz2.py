weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for element in weather_list:
    if element.isdigit():
        print(f'"{int(element):02d}"', end=" ")
    elif not element.isalnum():
        print("".join(f'"{element[0]}{int(element[1]):02d}"'), end="")
    else:
        print(element, end=" ")