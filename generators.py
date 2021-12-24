import hashlib

mystring = input('Введите путь к файлу ')


def get_md5():
    with open (mystring) as f:
        for line in f:
            yield hashlib.md5(line.encode()).hexdigest()

for item in get_md5():
    print(item)
