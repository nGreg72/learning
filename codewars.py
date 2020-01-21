"""сравнить длину списка исходных элементов с тем, сколько раз первый элемент входит в список.
Если эти значения равны, значит список состоит из одинаковых элементов."""

# def all_the_same(elements):
#     if len(elements) < 1:
#         return True
#     print(len(elements))
#     a = len(elements) == elements.count(elements[0])
#     return a

# ------------------------------------------------------------------------------------------------------
"""Другая особенность языка в том, что он предоставляет возможность умножать list на число и результатом этой операции 
будет list в котором все элементы скопированы указанное количество раз.
если умножить массив из одного первого элемента из исходного массива на длину этого исходного массива, 
то должен опять получиться исходных массив, если все элементы этого массива одинаковые. """


def all_the_same(elements):
    return not elements or [elements[0]] * len(elements) == elements


assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same(['a', 'a', 'a']) == True
assert all_the_same([]) == True
assert all_the_same([1]) == True
print("Coding complete? Click 'Check' to earn cool rewards!")

# ----------------------------------------------------------------------------------------------------------------------
import re

"""
def checkio(data):
    if len(data) <= 10:
        return False
    pattern = r"\d"


    return True or False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""
