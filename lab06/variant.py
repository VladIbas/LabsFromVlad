line = input().strip()
numbers = [int(x) for x in line.split()] if line else []
filtered = [x for x in numbers if x > 0]
print(filtered)
print(len(filtered))
print(sum(filtered))
print(sorted(filtered))