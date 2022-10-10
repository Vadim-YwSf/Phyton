#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве. 
#Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите координату по {xy[i]}:"))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Нужно ввести числа!")
    return a

def calcdistance(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance

print("Введите координаты точки А")
koordA = inputNumbers(2)
print("Введите координаты точки В")
koordB = inputNumbers(2)

print(f"Длина отрезка: {format(calcdistance(koordA, koordB), '.2f')}")