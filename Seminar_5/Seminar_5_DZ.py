'''Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.'''


def f(x, y):
    if y >= 1:
        return x * f(x, y - 1)
    elif y == 0:
        return 1
    else:
        print('Степень меньше нуля')
        return 0

A = int(input('Введите число А -> '))
B = int(input('Введите степень возведения числа А - число B -> '))
print('Результат равен = ', f(A, B))
