# -*- coding: utf-8 -*-

class MyClass1:
    a = 5
    b = 8
    c = 15

    def adder(self, v):
        return v + self.a   # передаём методу свойство КОНКТРЕТНОГО ОБЪЕКТА

    def subtractor(self, w):
        return self.c - w


obj1 = MyClass1()           # создаём объект класса
obj1.a = 25                 # переназначаем свойства ОБЪЕКТА и отправляем в метод adder класса myClass1 под именем self

obj2 = MyClass1()
obj2.a = 80


result1 = obj1.adder(10)     # передаём аргумент v в метод adder класса myClass1
result2 = obj2.adder(10)     #

# print(str(result1) + "\n" + str(result2))


# Класс как создатель объектов
class User:
    def setName(self, n):
        self.name = n
    def getName(self):
            try:
                return self.name
            except:
                print("No name")

first = User()

first.setName("Gregory")
print(first.getName())


# Конструктор класса. Автоматический вызов метода при создании объекта.
"""наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, что он принадлежит к группе методов перегрузки операторов."""
class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s


objDeskTable = Person("Greg", "Nick")    # автоматически передаём аргументы в метод класса без обращения к самому методу
print(objDeskTable.name, objDeskTable.surname)


"""Наследование классов"""
class Table:
    def __init__(self, l, w, h):
        self.lenth = l
        self.width = w
        self.hight = h

class KitchenTable(Table):      # Устанавливливаем связь с родительским классом
    def setPlace(self, p):                                                          # Чо это за херня? Как передать данные в параметр "p"?
        self.places = p

class DeskTable(Table):
    def square(self):
        return self.width * self.lenth


objDeskTable = DeskTable(2, 1.5, 0.5)
objKitchenTable = KitchenTable(2, 1.5, 0.5)
print(objDeskTable.square())
print("колво посадочных мест - " + str(objKitchenTable.setPlace(5)))

class MyClass:
    name = "Класс MyClass"
    def set(self, n):
        self.nickname = n
    def get(self):
        print("Значение поля : ", self.nickname)
    def __init__(self, n):
        self.set(n)
        print("Создан экземпляр класса")
        self.get()

green = MyClass("Зелёный")
print("Принадлежность : ", green.name)

red = MyClass("Красный")
print("Принадлежность", red.name)

MyClass.name = "Здесь могла быть ваша реклама !"
print("Спрашивает красный", red.name)
print("Спрашивает зелёный", green.name)

