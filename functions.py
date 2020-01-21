# -*- coding: utf-8 -*-

import copy
foo = 10
bar = 20


def my_eval():
    x = 10
    y = 15
    z = "x + y"
    print("Результат : ", z + " = ", eval(z))                               # z - это тип str, а eval(z) уже тип int
    return


def my_func1():
    print("this is func 1")
    print("it looks like working \n")


def my_func2():
    print("this is func 2")
    print("... and it's working also!")


def my_simple_calc():
    x = float(input('введите значение x ='))
    y = float(input('введите значение y ='))
    z = input('Введите оператор (+, -, *, /, mod, pow, div) =')

    if z == '+':
        result = x+y
    elif z == '-':
        result = x-y
    elif z == '*':
        result = x*y
    elif z == '/':
        result = x/y
    elif z == 'pow':
        result = pow(x,y)
    elif z == 'mod':
        result = x%y
    else:
        print("Чо за хуйню ты тут ввёл?")
        return

    print(str(result))


def my_for_func():
    for i in range(10):
        print(str(i) + " Хуйло Ворлд")
        # break                                             # break прервёт цикл. выполнится только одна итерация.

my_for_func()
def main():
    pass                                                  # это пустая функция.  pass не вызовет ошибку и скрипт продолжит выполнение.

def my_list_range():
    print(list(range(1, 6)))                                # визуализация виртуально последовательности функции range


pows_of_two = [2**i for i in range(15)]                     # генератор списка
print("Генератор списка : ", pows_of_two)
print(len(pows_of_two))

my_list = [1, 3, 5, 7, 9, 11, 3]
my_list_copy = my_list[:]                                   # Копия списка. переменные ссылаются на разные объекты
my_list_copy_2 = my_list.copy()                             # Копия списка. другой способ. переменные ссылаются на разные объекты
deepCopy = copy.deepcopy(my_list)                           # полная (глубокая) копия списка, включая элементы-списки
if my_list is my_list_copy:                                 # проверка списков на идентичность
    print("Ident")
else:
    print("Not ident")                                      # списки НЕ идентичны, т.к. это разные объекты

my_list.append(['a', 'b', 'c'])
print("добавление к концу списка" + str(my_list))

my_list.extend(['d', 'e', 'f'])
print("расширение списка " + str(my_list))

call_one_element = my_list[7][2]                            # вызов одного элемента из многомерного списка
print("вызов элемента из многомерного списка : ", call_one_element)

print("вхождение элемента в список ", 5 in my_list_copy)    # проверяем, входит ли элемент с указанным значением в список

print("индект элемента 7 ->", my_list_copy.index(7))        # узнаём индекс элемента 7

insert_one_element = my_list_copy.insert(2, ['x', 'y'])     # так делать нельзя.
my_list_copy.insert(2, ['x', 'y'])                          # эти операции должны быть выполнены "на месте"
print("вставка одного элемента " + str(my_list_copy))

print("количество элементов в списке : ", my_list.count(3)) # подсчёт элеменов в списке

my_list_copy.pop(6)                                         # удаление одного элемента списка по индексу
print(my_list_copy)                                         # функция pop возвращает результат. можно присваивать переменной

my_list_copy.remove(11)                                     # удаление элемента по значению
print(my_list_copy)                                         # результат НЕ возвращается

del my_list_copy[2:4]                                       # удаление среза списка с помощью функции del
print(my_list_copy)

"""Кортежи"""
a = (10, 20, 30)
b = (10,)                                                   # если не поставить запятую, кортеж не будет создан
c = 10, 20, 30
d = tuple([10, 20, 30])


"""Множества"""
a = set([1, 2, 3])                                          # создание множества
b = {2, 1, 3}
if a==b:
    print("True")
else:
    print("False")

a.add("a")                                                  # добавление к множеству
print("добавление к множеству :", a)

a.remove(3)
print("удаление из множества : ", a)                        # при удалении элемента, которого нет в списке, будет вызвана ошибка
a.discard(2)
print("удаление из множества : ", a)                        # при удалении элемента, которого нет в списке, ошибки не будет


"""Словари"""
my_dict = dict(первый="красный", второй="зелёный",          # создание словаря
               третий="синий")                              # ключ указыватеся без кавычек

my_dict_2 = {"первый":"красный", "второй":"зелёный",        # в такой записи используется двоеточие
             "третий":"синий"}                              # и название ключа в кавычках

print("элемент по ключу : ", my_dict["второй"])             # вызов элемента списка по ключу
print("элемент методом get : ", my_dict.get("второй"))      # если что, метод get не вызывает ошибку. возвращает None

my_dict["четвёртый"]="жёлтый"                               # добавление элемента в словарь
print("добавленный элемент : ", my_dict["четвёртый"])

