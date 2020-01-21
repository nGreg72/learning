def array_diff(a, b):
    res = list(set(a) ^ set(b))
    res = list(set(a + b))
    return res


a = [1, 1, 2, 1, 3]
b = [1, 3, 4]

# assert array_diff([1, 1, 2, 1, 3], [1, 3, 4])
assert array_diff([1, 1, 2, 1, 3], [])

# final = array_diff(a, b)
print("OK")
