# -*- coding: utf-8 -*-

"""Цикл с заданным количеством итераций"""
for i in range(1, 11):
    print(i)

#  ---------------------------------------------------------
"""Это docstring! """


def function(a, b, c):
    """Эта функция содержит многострочный докстринг.

    В многострочном докстринге первое предложение
    кратко описывает работу функции. Следующий
    за ним текст пишется через пустую строку, вот так.
    """
    pass


class UselessClass(object):
    """Это класс с докстрингом."""

    def method_of_class(self):
        """А это метод с докстрингом"""




# Для того чтобы увидеть результат работы мы можем выполнить несколько команд:

# import test_docstring
#
# print(test_docstring.__doc__)
# print(test_docstring.function.__doc__)
# print(test_docstring.UselessClass.method_of_class.__doc__)
# help(test_docstring.UselessClass)

# ----------------------------------------------------------------
