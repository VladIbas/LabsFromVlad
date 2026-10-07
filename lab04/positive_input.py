count = 0
while True:
    c = int(input("Введите целое число: "))
    if c > 0:
        break
    count += 1
print(f'Квадрат числа {c} это {c**2}')
print(f'кол-во отклонённых попыток - {count}')