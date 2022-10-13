# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.


num = int(input('Введите число организации списка: '))
import random
list = []
i = 0
for i in range (0, num*2+1):
    el = random.randint(-num, num)
    list.append(el)
    i += 1

print(list)

var = random.randint(2, 10)
temp_el = 0
while var > 0:
    for i in range(0, len(list)):
        for j in range(0, len(list) - i):
            temp_el = list[i]
            list[i] = list[j]
            list[j] = temp_el
        var -= 1

print(list)