line = input()
if not line.strip():
    original = []
    new_list = []
else:
    original = [int(x) for x in line.split()]
    new_list = [abs(x) for x in original]
print(original)
print(new_list)