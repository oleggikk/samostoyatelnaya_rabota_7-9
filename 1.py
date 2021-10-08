i = 0
def num_checker(a):
    global i
    if a.isdigit():
        i = int(a)
    else:
        try:
            i = float(a)
        except ValueError:
            print('Ошибка, вы ввели не числовое значение, не ввели его вовсе. Повторите попытку.')
    if i <= 0:
        print('Число должно быть положительным и неравным нулю. Повторите попытку.')
    return i
flag = True
while flag:
    A = num_checker(input('Введите значение А: '))
    if A > 0:
        flag = False
        i = 0
flag = True
while flag:
    B = num_checker(input('Введите значение B: '))
    if B > 0:
        flag = False
        i = 0
flag = True
while flag:
    C = num_checker(input('Введите значение C: '))
    if C > 0:
        flag = False
        i = 0
flag = True
while flag:
    D = num_checker(input('Введите значение D: '))
    if D > 0:
        flag = False
        i = 0
maxAB = max(A, B)
maxCD = max(C, D)
minAB = min(A, B)
minCD = min(C, D)
if (maxAB < maxCD) and (minAB < minCD):
    print('Прямоугольник со сторонами AB может разместиться внутри прямоугольника CD')
else:
    print('Прямоугольник со сторонами AB НЕ может разместиться внутри прямоугольника CD')