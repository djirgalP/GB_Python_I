'''Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.'''


def f(x, y):
    if y >= 1:
        return x * f(x, y - 1)
    elif y == 0:
        return 1
    else:
        return f(x, y + 1) / x

A = int(input('Введите число А -> '))
B = int(input('Введите степень возведения числа А - число B -> '))
print('Результат равен = ', f(A, B))


"""Задача 28:
Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы."""

def sum(a, b):
    if a > 0 and b >= 0:
        return 1 + sum(a - 1, b)
    elif a == 0 and b > 0:
        return 1 + sum(0, b - 1)
    elif a == 0 and b == 0:
        return 0

a = int(input('Введите целое неотрицательное число a -> '))
b = int(input('Введите целое неотрицательное число b -> '))
print('Результат суммы равен = ', sum(a, b))
