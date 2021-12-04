from itertools import zip_longest
import json
dict_value = {}
with open("users.csv", encoding="utf-8") as users:
    with open("hobby.csv", encoding="utf-8") as hobby:
        num_line_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_line_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            dict_value[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open("lesson_6_task_3", "w", encoding="utf-8") as f:
    json.dump(dict_value, f, ensure_ascii=False)
print(dict_value)
