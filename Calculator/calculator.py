from stack import Stack

def convert_to_polish(expression):
    temporary = []
    temporary_stack = Stack(len(expression))
    for i in range(len(expression)):
        priority = get_operation_priority(expression[i])
        if priority == 0:
            temporary.append(expression[i])
        if priority == 1:
            temporary_stack.push(expression[i])
        if priority >= 2:
            while not temporary_stack.isEmpty():
                if get_operation_priority(temporary_stack.peek()) >= priority:
                    temporary.append(temporary_stack.pop())
                else:
                    break
            temporary_stack.push(expression[i])
        if priority == -1:
            while get_operation_priority(temporary_stack.peek()) != 1:
                temporary.append(temporary_stack.pop())
            temporary_stack.pop()
    while not temporary_stack.isEmpty():
        temporary.append(temporary_stack.pop())
    return temporary

def calculate_polish(processed_expression):
    temporary_stack = Stack(len(processed_expression))
    for i in range(len(processed_expression)):
        if get_operation_priority(processed_expression[i]) == 0:
            temporary_stack.push(processed_expression[i])
        if get_operation_priority(processed_expression[i]) > 1:
            a = float(temporary_stack.pop())
            b = float(temporary_stack.pop())
            if processed_expression[i] == '+': temporary_stack.push(b + a)
            if processed_expression[i] == '-': temporary_stack.push(b - a)
            if processed_expression[i] == '*': temporary_stack.push(b * a)
            if processed_expression[i] == '/': temporary_stack.push(b / a)
    return temporary_stack.pop()

def get_operation_priority(operator):
    priority = 0
    if operator == ')':
        priority = -1
    if operator == '(':
        priority = 1
    if operator == '+' or operator == '-':
        priority = 2
    if operator == '*' or operator == '/':
        priority = 3
    return priority
