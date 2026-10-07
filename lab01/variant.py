name_order = input('Введите название заказа: ')
name_client = input('Введите имя заказчика: ')
pos1_name = input('Введите наименование первой позиции: ')
pos1_count = int(input(f'Введите количество ({pos1_name}): '))
pos1_price = float(input(f'Введите цену за единицу ({pos1_name}): '))
pos2_name = input('Введите наименование второй позиции: ')
pos2_count = int(input(f'Введите количество ({pos2_name}): '))
pos2_price = float(input(f'Введите цену за единицу ({pos2_name}): '))
delivery_price = float(input('Введите стоимость доставки: '))
summa = float(input('Введите внесённую сумму: '))
offpriceinput = int(input('Введите размер скидки от 0 до 100: '))
order1 = pos1_count * pos1_price
order2 = pos2_count * pos2_price
all_without_delivery = order1 + order2
discount_rub = all_without_delivery * (offpriceinput / 100)
goods_with_discount = all_without_delivery - discount_rub
total_with_delivery = goods_with_discount + delivery_price
all_count = pos1_count + pos2_count
change = summa - total_with_delivery
print(f"\nЗаказ: {name_order}")
print(f"Заказчик: {name_client}")
print(f"{pos1_name} | {pos1_count} | {pos1_price:.2f} | {order1:.2f}")
print(f"{pos2_name} | {pos2_count} | {pos2_price:.2f} | {order2:.2f}")
print(f"Стоимость товаров без доставки: {all_without_delivery:.2f}")
print(f"Скидка ({offpriceinput}%): {discount_rub:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_with_discount:.2f}")
print(f"Стоимость с доставкой (Итого к оплате): {total_with_delivery:.2f}")
print(f"Общее количество единиц: {all_count}")
print(f"Сдача: {change:.2f}")