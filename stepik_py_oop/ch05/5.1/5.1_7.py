# считывание строки и разбиение ее по пробелам
# lst_in = input().split()

lst_in = "8 11 abcd -7.5 2.0 -5".split()


def is_int(x):
    try:
        int(x)
    except:
        return False
    return True


res = sum(map(int, list(filter(lambda x: is_int(x), lst_in))))
print(res)
