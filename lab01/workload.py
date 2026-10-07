first_lesson = input('Введите название первого предмета: ')
count_lesson_first = int(input(f'Кол-во занятий по первому предмету({first_lesson}) в неделю: '))
count_time_first = int(input(f'Введите продолжительность одного занятия по {first_lesson} (в минутах): '))
second_lesson = input('Введите название второго предмета: ')
count_lesson_second = int(input(f'Кол-во занятий по второму предмету({second_lesson}) в неделю: '))
count_time_second = int(input(f'Введите продолжительность одного занятия по {second_lesson} (в минутах): '))
free_time = float(input('Введите доступное время на неделю в часах: '))
time_first_min = count_lesson_first * count_time_first
time_second_min = count_lesson_second * count_time_second
total_time_min = time_first_min + time_second_min
total_time_hours = total_time_min / 60
remaining_free_hours = free_time - total_time_hours
four_weeks_hours = total_time_hours * 4
print("\n--- Результаты расчёта ---")
print(f"Время по предмету '{first_lesson}': {time_first_min} мин.")
print(f"Время по предмету '{second_lesson}': {time_second_min} мин.")
print(f"Общая нагрузка за неделю: {total_time_min} мин. ({total_time_hours:.2f} ч.)")
print(f"Остаток свободного времени: {remaining_free_hours:.2f} ч.")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч.")