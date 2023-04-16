x = int(input('Type a number from 0 to 8639999:'))
if x < 0 or x >= 8640000:
    print('invalid number')
else:
    m = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    a = x // (60 * 60 * 24)
    b = (x - a * (60 * 60 * 24)) // (60 * 60)
    c = (x - a * (60 * 60 * 24) - b * (60 * 60)) // 60
    d = x - a * 60 * 60 * 24 - b * 60 * 60 - c * 60
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    b = b.zfill(2)
    c = c.zfill(2)
    d = d.zfill(2)
    if len(a) == 2 and int(a) // 10 == 1:
        print(f'{a} дней, {b}:{c}:{d}')
    elif int(a) % 10 == 2 or int(a) % 10 == 3 or int(a) % 10 == 4:
        print(f'{a} дня, {b}:{c}:{d}')
    elif int(a) % 10 == 1:
        print(f'{a} день, {b}:{c}:{d}')
    else:
        print(f'{a} дней, {b}:{c}:{d}')
