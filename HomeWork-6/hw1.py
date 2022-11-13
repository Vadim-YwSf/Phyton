#Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions
n = int(input(f'Ведите значение числа N: '))
numbers_list = [el for el in range (n) if el % 2 != 0 and el * el < 200]
print(numbers_list)