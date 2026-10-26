line = input().strip()
if not line:    print("Нет данных")
else:
    numbers = [int(x) for x in line.split()]    
    if not numbers:     print("Нет данных")
    else:
        max_val = max(numbers)
        indices = []
        
        for i, val in enumerate(numbers):
            if val == max_val:
                indices.append(i)

        print(indices)