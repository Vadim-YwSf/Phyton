#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

check = int(input('Введите номер четверти: '))

match check:
    case 1:
        print('Значения Х от 0 до +бесконечности, значения Y от 0 до +бесконечности.')
    case 2:
        print('Значения Х от -бесконечности до 0, значения Y от 0 до +бесконечности.')
    case 3:
        print('Значения Х от -бесконечности до 0, значения Y от -бесконечности до 0.')
    case 4:
        print('Значения Х от 0 до +бесконечности, значения Y от -бесконечности до 0.')
    case _:
        print('Такой четверти не существует.')