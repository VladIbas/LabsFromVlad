c1 = float(input("Введите первое число: "))
c2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ").strip()
if operation == "-":
    result = c1 - c2
    print(f"{result:.2f}")
elif operation == "+":
    result = c1 + c2
    print(f"{result:.2f}")
elif operation == "*":
    result = c1 * c2
    print(f"{result:.2f}")
elif operation == "/":
    if c2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = c1 / c2
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")