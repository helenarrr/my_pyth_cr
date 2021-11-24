

def thesaurus(*names):
    staff_dict = {}
    for name in names:
        staff_dict.setdefault(name[0], [])
        staff_dict[name[0]].append(name)
    return staff_dict


print(thesaurus("Маша", "Михаил", "Иван", "Елена", "Петр"))