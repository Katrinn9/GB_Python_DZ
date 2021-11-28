# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных
# в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

# f = open('user.csv', 'w', encoding='utf-8')
# print('Иванов,Иван,Иванович\nПетров,Петр,Петрович', file=f)
# f.close()
#
# f = open('hobby.csv', 'w', encoding='utf-8')
# print('скалолазание,охота\nгорные лыжи', file=f)
# f.close()


from itertools import zip_longest
import json
voc = {}
with open('user.csv', encoding='utf-8') as user, open('hobby.csv', encoding='utf-8') as hobby:
    num_line_user = sum(1 for line in user)
    num_line_hobby = sum(1 for line in hobby)

    if num_line_user < num_line_hobby:
        exit(1)

    user.seek(0)
    hobby.seek(0)
    for line_user, line_user_hobby in zip_longest(user, hobby):
        voc[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(voc, f, ensure_ascii=False)
print(voc)
