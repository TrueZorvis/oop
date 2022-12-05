def input_int_numbers():
    nums = input().split()
    try:
        res = [int(n) for n in nums]
    except:
        raise TypeError('все числа должны быть целыми')
    return tuple(res)


while True:
    try:
        result = input_int_numbers()
    except TypeError:
        continue
    else:
        print(*result)
        break

print('end')
