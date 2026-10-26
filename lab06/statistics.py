line = input().strip()

if not line:
    print("Нет данных")
else:
    parts = line.split()
    if not parts:
        print("Нет данных")
    else:
        count = 0
        total = 0
        minimum = None
        maximum = None
        
        for part in parts:
            num = int(part)
            total += num
            count += 1
            
            if minimum is None or num < minimum:
                minimum = num
            if maximum is None or num > maximum:
                maximum = num
                
        average = total / count
        
        print(count)
        print(total)
        print(minimum)
        print(maximum)
        print(f"{average:.2f}")