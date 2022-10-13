#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:- 6782 -> 23    - 0,56 -> 11   - 187,6778 -> 44

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = input_numbers("Введите число: ")

print(f"Сумма цифр = {sum_nums(num)}")