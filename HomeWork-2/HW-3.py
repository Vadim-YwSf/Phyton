#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
#Пример: Для n=4 [2, 2.25, 2.37, 2.44]  Сумма 9.06

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Число должно быть Целым!")
    return number

def mult(n):
    if n == 1:
        return 2
    else:
        return round((1+1/n)**n , 2)

num = input_numbers("Введите число:")

list = []
for x in range(1, num + 1):
    list.append(mult(x))

sum_elements = 0
for i in range(len(list)):
    sum_elements += list[i]

print(f"Сумма чисел в последовательности {list} = {sum_elements}")