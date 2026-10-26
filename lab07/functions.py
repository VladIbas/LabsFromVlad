def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def average(numbers):
    """Возвращает среднее арифметическое или None для пустого списка."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    """Приводит текст к нижнему регистру, удаляет краевые пробелы и схлопывает внутренние."""
    return " ".join(text.split()).lower()

def select_numbers(numbers, threshold):
    """Возвращает новый список чисел, значения которых не больше порога."""
    return [x for x in numbers if x <= threshold]