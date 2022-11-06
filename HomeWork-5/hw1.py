#Напишите программу, удаляющую из текста все слова, содержащие "abc".
#Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
#Использовать вложенный менеджер контекста

from asyncore import read

with open('file_hw1', 'w') as opened_file:
    opened_file.write('ываабв лповап абвцукв алоабвабв ываываыв')

with open('file_hw1', 'r') as opened_file:
   text = opened_file.read()

print(text)

find_text = "абв"

lst = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')

with open('file_hw_res', 'w') as opened_file:
    opened_file.write(" ".join(lst))