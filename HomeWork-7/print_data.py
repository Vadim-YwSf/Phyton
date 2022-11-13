#модуль печати контакта

def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Телефон".center(10), "Примечание".center(15))
        print("-"*60)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(10), item[3].center(15))
    else:
        print("Справочник пуст!")