#Задача 2

print('Please, enter any number -> ', end='')
chislo = str(input())
sum = 0
for i in range(len(chislo)):
    sum += int(chislo[i])
print('The result is ', sum)

#Задача 4

print('Please, enter the number of  cranes -> ', end='')
total = int(input())
petya = total // 6
katya = 2 * 2 * petya
print('The result is {} {} {}'.format(petya, katya, petya))

#Задача 6
print('Please, enter any ticket number -> ', end='')
ticket = str(input())
if len(ticket) != 6:
    print('no')
else:
    sum1 = 0
    sum2 = 0
    for i in range(len(ticket) - 3):
        sum1 += int(ticket[i])
    for j in range(3, len(ticket)):
        sum2 += int(ticket[j])
    if sum1 != sum2:
        print('no')
    else:
        print('yes')

#Задача 8

n, m, k = map(int, input("Please, enter values for n, m, k using a space: ").split())
if (k % n == 0 or k % m == 0) and k <= n * m:
    print('yes')
else:
    print('no')
