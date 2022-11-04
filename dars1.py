""" Списки """



names = ["Кеша", "Толик", "Попугай"]
print(names[1])
print(names[-1])

for name in names:
    print(name)
names.pop()
print(names)

names.append("Jorj")
print(names)

n = names.index("Кеша")
print(n)

print(len(names))

numbers = [4, 6, 81, 95, 108, 56]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers[1] = "b"
print(numbers)

letters = ["a", "c", "b", "d"]
letters.sort()
print(letters)

