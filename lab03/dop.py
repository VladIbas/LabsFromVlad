count = int(input("Введите год от 1 до 9999: "))
if count % 400 == 0 or (count % 100 != 0 and count % 4 == 0): print('Год високосный')
else: print('Год не високосный')