from datetime import datetime

"""Декоратор"""
def timing(func):
    def timecounters():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result

    return timecounters


"""Генератор чисел"""
@timing
def generate():
    digits = [i for i in range(1000000) if i % 2]
    return digits


# l1 = generate()
l1 = timing(generate)
print(l1)
