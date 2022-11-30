# 1. Model:
# Функция преобразования: Вход: str = "7/65", Выход: list = [7, 65] DONE
# Функция вычисления общего знаменателя: Вход: 2 int, Выход: 1 int (общий знаменатель)
# Вычисление коэффициента для умножения 2 дробей
# Функция calculate (выполнения матем.действия): Вход: 2 list (рациональных числа), операция: str (+,-), Выход: список (результат)


def from_user_data_to_list(user_data: str) -> list:
    elem = []
    if "/" in user_data:
        elem = user_data.split("/")
        return list(map(int,elem))
    else:
        return [int(user_data), 1]

def smallest_denominator(number_1, number_2: list) -> int:
    sml_d = max(number_1[1], number_2[1])
    while ((sml_d % number_1[1] != 0) or (sml_d % number_2[1] != 0)):
        sml_d += 1
    return sml_d

def calculate(operator: str, num_1: list, num_2: list):
    result = []
    if operator == '/':
        result[0] = num_1[0] * num_2[1]
        result[1] = num_1[1] * num_2[0]
        return result
    elif operator == '+':
        result[1] = smallest_denominator(num_1[1], num_2[1])
        result[0] = (((result[1]/num_1[1])) * num_1[0]) + ((result[1]/num_2[1]) * num_2[0])
        return result
    elif operator == '-':
        result[1] = smallest_denominator(num_1[1], num_2[1])
        result[0] = (((result[1]/num_1[1])) * num_1[0]) - ((result[1]/num_2[1]) * num_2[0])
        return result
    elif operator == '*':
        result[0] = num_1[0] * num_2[0]
        result[1] = num_1[1] * num_2[1]
        return result
    else: print('Что-то введено некорректно')

