# Реализация пользовательского stack в Python
class Stack:

    # Конструктор для инициализации stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    # Функция добавления элемента val в stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)

        #print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val

    # Функция для извлечения верхнего элемента из stack
    def pop(self):
        # проверка на опустошение stack
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)

        #print(f'Removing {self.peek()} from the stack')

        # уменьшает размер stack на 1 и (опционально) возвращает извлеченный элемент
        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    # Функция для возврата верхнего элемента stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    # Функция возврата размера stack
    def size(self):
        return self.top + 1

    # Функция для проверки, пуст stack или нет
    def isEmpty(self):
        return self.size() == 0

    # Функция проверки заполнения stack.
    def isFull(self):
        return self.size() == self.capacity