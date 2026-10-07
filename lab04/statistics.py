n = int(input())
max_val = float('-inf')
count_pos = 0
summa = 0
for i in range(n):
    c = int(input())
    summa += c
    if c > 0:
        count_pos += 1
    if c > max_val:
        max = c
print(f'сумма: {summa}')
print(f'кол-во положительных: {count_pos}')
print(f'максимальное: {max_val}')