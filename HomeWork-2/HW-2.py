#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

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
        return 1
    else:
        return n * mult(n - 1)

num = input_numbers("Введите число:")

list = []
for x in range(1, num + 1):
    list.append(mult(x))

print(f"Произведения чисел от 1 до {num}:  {list}")