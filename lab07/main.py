from functions import average, normalize_text, select_numbers, sum_digits

def main():
    # 1. Сумма цифр
    num = int(input())
    print(sum_digits(num))

    # 2. Среднее и отбор по порогу (вариант 5)
    line = input().strip()
    numbers = [int(x) for x in line.split()] if line else []

    avg = average(numbers)
    if avg is None:
        print("Нет данных")
    else:
        print(avg)

    threshold = int(input())
    print(select_numbers(numbers, threshold))

    # 3. Нормализация текста
    text = input()
    print(normalize_text(text))


if __name__ == "__main__":
    main()