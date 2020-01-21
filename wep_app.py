import hashlib

file = open('anekdot.txt', 'rb').read()
h = hashlib.md5(file).hexdigest()

print(h)