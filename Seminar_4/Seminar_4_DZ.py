'''Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.
Input: 11 6
(значения сгенерированы случайным образом
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18)
Output: 11 6
6 12'''
import random
n = int(input('Введите количество элементов первого набора чисел -> '))
m = int(input('ведите количество элементов второго набора чисел ->'))
array_n = []
array_m = []
for i in range(n):
    random_number = round(random.randint(1, 30))
    array_n.append(random_number)
print(*array_n, sep=' ')
for i in range(m):
    random_number = round(random.randint(1, 30))
    array_m.append(random_number)
print(*array_m)
set_n = set(array_n)
#print(set_n)
set_m = set(array_m)
#print(set_m)
final_list = sorted(set_n.intersection(set_m))
if not final_list:
    print('Пересечений нет')
else:
    print(*final_list, sep=' ')
'''Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. '''

N = int(input("Введите количество кустов черники -> "))
blueberry = []
for i in range(N):
    random_number = round(random.randint(1, 10))
    blueberry.append(random_number)
print(*blueberry, sep=' ')

max_blueberry = 0
for k in range(-N + 1, 1, 1):
    #print('k = ', k)
    amount_of_blueberry = blueberry[k - 1] + blueberry[k] + blueberry[k + 1]
    #print('amount_of_blueberry', amount_of_blueberry)
    if max_blueberry < amount_of_blueberry:
        max_blueberry = amount_of_blueberry

print('Максимальное число ягод = ', max_blueberry)