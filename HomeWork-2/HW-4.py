#Задайте список из элементов, заполненных числами из промежутка [-N, N]. 
#Задайте два числа - позиции(индексы) в исходном списке это границы диапазона. 
#Найдите произведение элементов списка в указанном диапазоне индексов
#Пример: N = 6 Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
#границы диапазона: 2, 5
#Произведение для [4, 1, 4, 1] равно 16
#Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, что они могут быть некорректными: больше длины списка, меньше нуля, первый больше второго и т.п.

import numpy as np

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


num = input_numbers("Введите число для промежутка чисел:")
list = []

i = 0
for i in range (0, num*2+1):
    el = np.random.randint(-num, num)
    list.append(el)
    i += 1
    
print(list)

pos_1 = int(input('Введите 1-у позицию: '))
pos_2 = int(input('Введите 2-у позицию: '))
mult_list = []

if pos_1 > num*2 or pos_2 > num*2: 
    print('Один или оба индекса не существуют в списке')
elif pos_1 < pos_2:
    for i in range (pos_1, pos_2+1):
        mult_list.append(list[i])
else:
    for i in range (pos_2, pos_1+1):
        mult_list.append(list[i])

mult = 1

for el in mult_list:
    mult = mult * el

print(mult_list)
print(f"Произведение элементов между {pos_1} и {pos_2}  равно {mult}")
