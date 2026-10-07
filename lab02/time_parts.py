total_seconds = int(input('Введите время(в секундах): '))
seconds = total_seconds % 60
all_minuts = (total_seconds % 3600) // 60
hours = total_seconds // 3600
print(f'{total_seconds} секунд, это {hours} час, {all_minuts} минут и {seconds} секунд')