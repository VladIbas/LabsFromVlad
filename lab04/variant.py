n = int(input())
count = 0
summa_val = 0
for i in range(n):
    x = int(input())
    if x >= 10:
        count += 1
        summa_val += x
print(f'Кол-во чисел удов. условие - ({count})\nИх сумма - ({summa_val})')