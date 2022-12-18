'''Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.'''
import random
print('Please, enter number of coins -> ', end='')
n = int(input())

orel = 0
reshka = 0

for i in range(n):
    random.seed()
    random_number = random.randint(0, 1)
    print(random_number, end=' ')
    if random_number == 1:
        orel += 1
    else:
        reshka += 1

if orel <= reshka:
    print('\n Number of coins to turn over: ', orel)
else:
    print('\n Number of coins to turn over: ', reshka)

'''Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.'''
S, P = map(int, input("Please, enter values S and P using a space: ").split())
# X + Y = S
# X * Y = P
# Y = S - X
# X**2 - S*X - P = 0


'''Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''
print('Please, enter N  -> ', end='')
N = int(input())
number = 2
stepen = 1
result = number ** stepen
while result <= N:
    print(result, end = ' ')
    stepen += 1
    result = number ** stepen
