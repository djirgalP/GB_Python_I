def read_data_from_file(file_name):
    list_of_rows = []
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            list_of_rows.append(line.strip('\n').split(','))
        return list_of_rows


def save_data_to_file(file_name, list_of_rows):
    with open(file_name, 'w', encoding='utf8') as file:
        for each_data in list_of_rows:
            file.write(','.join(each_data)+'\n')


def add_item_to_file(name, new_data):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(','.join(new_data)+'\n')
    print("Запись {} успешно добавлена".format(new_data))


def get_item_by_id(id, data):
    for id_record, item_record1, item_record2 in data:
        item_record = []
        if id == id_record:
            item_record.append(item_record1)
            item_record.append(item_record2)
            print("item_record = ", item_record1, item_record2)
            return item_record
            break
    return None


def print_bus():
    bus = read_data_from_file('bus.txt')
    print('|Идентификатор|      Марка|    Номер|')
    print('-'*38)
    for ids, marka, number in bus:
        print('|{:>14s}|{:>11s}|{:>9s}|'.format(ids, marka, number))
    input("Enter>")


def add_bus():
    ids = input('Введите идентификатор автобуса:')
    marka = input("Введите Марку: ")
    number = input("Введите Гос. номер: ")
    add_item_to_file('bus.txt', [ids, marka, number])


def print_driver():
    drivers = read_data_from_file('driver.txt')
    print('|Идентификатор|     Фамилия|       Имя|')
    print('-'*40)
    for ids, firstname, lastname in drivers:
        print('|{:>14s}|{:>12s}|{:>10s}|'.format(ids, lastname, firstname))
    input("Enter>")


def add_driver():
    driver_id = input('Введите Идентификатор:')
    lastname = input('Введите Фамилию:')
    firstname = input("Введите Имя: ")
    add_item_to_file('driver.txt', [driver_id, lastname, firstname])


def print_route():
    routes = read_data_from_file('marshrut.txt')
    buses = read_data_from_file('bus.txt')
    drivers = read_data_from_file('driver.txt')
    print('|Маршрут|   №|Фамилия водителя|Имя водителя|Марка автобуса| Госномер|')
    print('-'*62)
    for r_name, r_number, r_bus, r_driver in routes:
        driver = []
        bus = []
        bus = get_item_by_id(r_bus, buses)
        driver = get_item_by_id(r_driver, drivers)
        print('|{:>7}|{:>4}|{:>16}|{:>12}|{:>14}|{:>9}|'.format(r_name, r_number, driver[0], driver[1], bus[0], bus[1]))
    input("Enter>")


def add_route():
    route_id = input('Введите Идентификатор маршрута:')
    route_number = input("Введите Номер маршрута: ")
    driver_id = input("Введите Идентификатор водителя: ")
    bus_id = input("Введите Идентификатор автобуса: ")
    add_item_to_file('marshrut.txt', [route_id, route_number, driver_id, bus_id])

