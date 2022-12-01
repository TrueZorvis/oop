# считывание строки и разбиение ее по пробелам
# lst_in = input().split()

lst_in = "1 -5.6 True abc 0 23.56 hello".split()


def is_digit(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


lst_out = list(map(is_digit, lst_in))
print(lst_out)
