#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibon_pos(n):
    if n < 3:
        return 1
    return fibon_pos(n - 1) + fibon_pos(n - 2)

def fibon_neg(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return fibon_neg(n + 2) - fibon_neg(n + 1)

number = int(input('Введите число: '))

if number > 0: number = -number
temp = - number
fibonacci = []
f_e = ''

while number < 0:
    f_e = fibon_neg(number)
    fibonacci.append(f_e)
    number += 1
fibonacci.append(0)

fibonacci_temp = []
while temp > 0:
    f_e = fibon_pos(temp)
    fibonacci_temp.append(f_e)
    temp -= 1
fibonacci_temp.reverse()

fibonacci += fibonacci_temp
print(fibonacci)