from functions import average, normalize_text, select_numbers, sum_digits

# Базовые тесты sum_digits
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

# Базовые тесты average
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9

# Базовые тесты normalize_text
assert normalize_text("  ПРИВЕТ    Мир  ") == "привет мир"
assert normalize_text("    ") == ""

# Тесты для Варианта 5 (Не больше порога: x <= threshold)
test_list = [-5, 0, 2, 5]
copy_list = list(test_list)

# Проверка контрольного примера (порог 2)
assert select_numbers(test_list, 2) == [-5, 0, 2]

# Проверка того, что исходный список не изменился
assert test_list == copy_list

# Проверка пустого списка и пустого результата
assert select_numbers([], 2) == []
assert select_numbers([3, 4, 5], 2) == []

# Проверка сохранения повторов и работы с граничными значениями
assert select_numbers([-2, -2, 2, 2, 4], 2) == [-2, -2, 2, 2]

print("Все проверки успешно пройдены!")