

def thesaurus_adv(*names_surnames):
    staff_dict = {}
    for names_surname in names_surnames:
        name, surname = names_surname.split()
        staff_dict.setdefault(surname[0], {})
        staff_dict[surname[0]].setdefault(name[0], [])
        staff_dict[surname[0]][name[0]].append(names_surname)
    return staff_dict


print(thesaurus_adv("Михаил Степанов", "Павел Назаров", "Елена Иванова"))