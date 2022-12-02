a, b = input().split()

try:
    res = int(a) + int(b)
except:
    try:
        res = float(a) + float(b)
    except:
        res = str(a) + str(b)
finally:
    print(res)
