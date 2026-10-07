price = int(input('Введите цену одной тетрадки: '))
count = int(input('Введите кол-во тетрадей: '))
paid = int(input('Введите переданную сумму: '))
print(f"Стоимость - {(price*count)} рублей \nСдача - {(paid - (price*count))} рублей")