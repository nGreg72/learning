"""Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
даже если это часть другого слова. Все строки даны в нижнем регистре.
Входные данные: Последовательность строк, как кортеж строк (юникод).
Выходные данные: Текст, как строка.
Предусловие:
0 < len(phrases) < 42"""


def left_join(phrases: str):
    """ Join strings and replace "right" to "left" """
    # phrases = str(phrases)
    string = ",".join(phrases).replace("right", "left")
    return str(string)


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
