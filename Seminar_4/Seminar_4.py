'''Задача 25: Напишите прогр кот принимает на вход строку и отслеживает сколько раз каждый символ УЖЕ встречался.
количество повторов добавляется к каждому символу на выходе через постфикс формата _n
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''
stroka = input().split()
print(stroka)
stroka_dic = dict()
for element in stroka:
    if element not in stroka_dic:
        print(element, end=' ')
        stroka_dic[element] = 1
    elif element in stroka_dic:
        print('{}_{}'.format(element, stroka_dic[element]), end=' ')
        stroka_dic[element] += 1
#print(stroka_dic)
