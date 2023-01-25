fileName = 'tel.txt'


def addContact(file_name, user_data):
    with open(file_name, 'a') as data:
        data.writelines(user_data + '\n')


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result


def printFile(file_name):
    f = ""
    with open(file_name, 'r+') as data:
        for line in data:
            f += line
    print(f)


def findUserByName(file_name, person_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    counter = 0
    for person in result:
        if (person[0].find(person_name) >= 0) or (person[1].find(person_name) >= 0) or (person[2].find(person_name) >= 0):
            #return person
            counter += 1
            print(person[0], person[1], person[2], person[3])
    print('Всего найдено совпадений:', counter)

def findUserByPhone(file_name, phone):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    counter = 0
    for person in result:
        if person[3].find(phone) >= 0:
            counter += 1
            print(person[0], person[1], person[2], person[3])
    print('Всего найдено совпадений по телефону:', counter)


def deleteUserByAnyString(file_name, str):
    new_lines = ""
    with open(file_name, 'r') as data:
        for line in data:
            if str not in line:
                new_lines += line
                # print(line)
    with open(file_name, 'w') as data:
        data.write(new_lines)

addContact(fileName, 'Poshtarova, Djirgal, Igorevna, +79261717503')
show_flag = True
menu = '1 - Показать все записи \n2 - Найти запись по вхождению частей имени\n3 - Найти запись по телефону\n4 - Добавить новый контакт\n5 - Удалить контакт\n7 - Выход\n '
while (show_flag):
    print(menu)
    chosen_menu = int(input('>:'))

    if chosen_menu == 1:
        #вывод данных
        printFile(fileName)
    elif chosen_menu == 2:
        #найти запись по вхождению частей имени
        name = str(input('Введите имя или его часть для поиска контакта: '))
        findUserByName(fileName, name)
    elif chosen_menu == 3:
        #Найти запись по телефону
        phone = input('Введите номер телефона или его часть для поиска контакта: ')
        findUserByPhone(fileName, phone)
    elif chosen_menu == 4:
        #добавить новый контакт
        new_person_surname = str(input('Введите Фамилию: '))
        new_person_name = str(input('Введите Имя: '))
        new_person_name2 = str(input('Введите Отчество: '))
        new_person_phone = str(input('Введите Телефон: '))
        addContact(fileName, new_person_surname+', ' + new_person_name + ', ' + new_person_name2 + ', ' + new_person_phone)
    elif chosen_menu == 5:
        #удалить контакт
        part = str(input('Введите часть имени или номера для удаления контакта: '))
        deleteUserByAnyString(fileName, part)
    # elif chosen_menu == 6:
    #изменить номер телефона

    else:
        #выход
        print('Завершение')
        show_flag = False

# addContact(fileName, 'Poshtarova, Djirgal, Igorevna, +79261717503')
# print(readFile(fileName))
# print(findUserByPhone(fileName, '79999999999'))
# print(findUserByName(fileName, 'Dji'))
# deleteUserByAnyString(fileName, 'Djirgal')