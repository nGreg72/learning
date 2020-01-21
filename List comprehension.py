from phones import google_phones
from phones import phone_dict
from transliterate import translit, get_available_language_codes

first_list = {
    "first_name": "test1",
    "second_name": "test2",
    "third_name": "test3"
}

second_list = {
    "first_name": "fuck1",
    "second_name": "fuck2",
    "third_name": "fuck3"
}

third_list = {
    "first_name": "shit1",
    "second_name": "shit2",
    "third_name": "shit3"
}

LIST = [first_list, second_list, third_list]

"""Обычный способ"""
# item = []
#
# for i in LIST:
#     item.append(i['first_name'])

"""Сокращённый способ"""
# first_item = [i['first_name'] for i in LIST]
# first_item = [i.get('first_name', 'нету нихуяшеньки') for i in LIST]

"""Фильтрация"""
# first_item = [i for i in google_phones if i.title().startswith('Al')]

"""На основе этого фильтра (.count) можно сделать нестрогий поиск. Например, поиск пользователей"""

# find_me = input("Поиск :")
# find_me = find_me.lower()
#
# def search(find_me):
#     first_item = [i for i in google_phones if i.lower().count(find_me)]
#     return first_item
#
# result = search(find_me)
# print(result)


"""Цикл словаря по ключам и значениям"""

for key, value in phone_dict.items():
    print(value)

# userstring = str(input("Вводи сюда чо-нибудь:"))
# newname = translit("Вводи сюда чо-нибудь:", 'ru', reversed=True)
# print(newname)


