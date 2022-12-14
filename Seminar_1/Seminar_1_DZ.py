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
