# 3. View - модуль взаимодейчствия с пользователем
# Функция ввода данных - 2 шт (число +оператор) DONE
# Функция печати рационального числа

def hello():
    print('Привет! Давай займемся вычислениями с простыми дробями! Вводи дроби в формате ХХ/ХХ.')

def element_input():
    return str(input("Введите число: "))

def operator_input():
    return input("Введите операцию: ")

def result_print(num_1: list, num_2: list, operator: str, result: list):
    print(f'Результат вычисления {num_1[0]}/{num_1[1]} {operator} {num_2[0]}/{num_2[1]} равен {result[0]}/{result[1]}')


