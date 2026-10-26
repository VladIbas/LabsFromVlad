original = input()
output = ""
count = 0
for word in original.split():
    cleaned = word.strip(".,!?;:").lower()
    if cleaned:
        if 3 <= len(cleaned) <= 5:
            output += cleaned + "\n"
            count += 1
if count == 0:
    print("Нет совпадений")
    print(count)
else:
    print(output, end="")
    print(count)