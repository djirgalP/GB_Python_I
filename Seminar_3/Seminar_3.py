'''17
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''
# import random
#
# n = int(input('Введите длину списка >>> '))
# l = []
# for num in range(0,n):
#
#     random_number = round(random.randint(0,5))
#     l.append(random_number)
#
# a = set(l)
#
# print(l)
# print(len(a))
'''19
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  
K – положительное число.

Input:   [1, 2, 3, 4, 5] k = 2

Output:  [4, 5, 1, 2, 3]'''
# n = int(input('Введите длину списка >>> '))
# l = []
# for num in range(0,n):
#
#     random_number = round(random.randint(-10,10))
#     l.append(random_number)
# print(l)
#
# k = int(input('Введите на сколько индексов сдвигать >>> '))
# for i in range(k):
#     p = l.pop(-1)
#     l.insert(0, p)
#
# print(l)

'''Напишите программу для печати всех уникальных значений в словаре. 
Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
inpDict = {
    "I": "S001",
    "II": "S002",
    "III": "S001",
    "IV": "S005",
    "V": " S005 ",
    "VI": " S009 ",
    "VII": " S007 ",
}


res = set(inpDict.values())

print(inpDict.values(), "\n")
print(sorted(res))

'''inpDict = {"I": "S001","II": "S002", "IV": "S005","V": " S005 ","VI": " S009 ","VII": " S007 ",}

res = set(inpDict.values())

print(inpDict.values(),"\n")
print(sorted(res))
'''

'''
23
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3]
Output: 2 
пояснение
(-1 < 5, 2 < 3)
'''
array = [0, 1,2,3,4,5,6]
count = 0
for i  in range(0, len(array)-1):
    if array[i-1 < array[i+1]]:
        count += 1
print(array)
print(count)


