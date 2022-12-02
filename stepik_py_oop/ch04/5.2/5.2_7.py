def get_loss(w1, w2, w3, w4):
    y = 10 * w1
    try:
        y = y // w2
    except:
        return "деление на ноль"
    else:
        y = y - 5 * w2 * w3 + w4
    return y


r = get_loss(1, 3, 5, 10)
print(r)
