'''Задача 2
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''
print('Please, enter any number -> ', end='')
chislo = str(input())
sum = 0
for i in range(len(chislo)):
    sum += int(chislo[i])
print('The result is ', sum)

'''Задача 4
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
 а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?'''
print('Please, enter the number of  cranes -> ', end='')
total = int(input())
petya  = total / 6
katya = 2 * 2 * petya
print('The result is  {} + {} + {}'.format(petya, katya, petya))