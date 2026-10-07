# Вариант 7
count = int(input("Введите процент прочитанности книги: "))
if 0 <= count <= 9: print('Начало')
elif 10 <= count <= 89: print('Чтение')
elif 90 <= count <= 100: print('Почти готово')
else: print('Ошибка диапазона')