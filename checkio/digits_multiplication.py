"""Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).
Входные данные: Положительное целое число.
Выходные данные: Произведение цифр как целочисленное (int).
Предусловия: 0 < number < 106"""


def checkio(number: int) -> int:

    result = 1              # Объявляем стартовую переменную. С неё начнём умножение элементов массива.

    for i in str(number):   # Так как на входе тип int, меняем его на str. Ибо int -  не итерируемый объект.
        n = int(i)          # После разложения массива на составляющие, вертаем каждый элемент обратно в int, т.к. будем работать с математикой.
        if n != 0:
            result *= n
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
