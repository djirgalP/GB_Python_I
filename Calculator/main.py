import calculator as calc

if __name__ == "__main__":
    print('Введите математическое выражение: ', end='')
    expression_array = str(input()).split()
    #print(expression_array)
    print(calc.calculate_polish(calc.convert_to_polish(expression_array)))
