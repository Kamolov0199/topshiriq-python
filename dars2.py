""" Кортежи """
tuple = ("First", 25, 21.1,)
tuple[1] = 58
print(tuple)

tuple = ("First")
print(type(tuple))

tuple1 = ("First",)
print(type(tuple1))

print(tuple([45, 45, 147, 45]))

print(list((45, 45, 147, 45)))


""" Словари """

dict = {"Яблоко": "красное", "банан": "желтый", "лимон": "желтый"}
print(dict)

for x in dict.keys():
    print(x)

for x in dict.values():
    print(x)

for k in dict.items():
    print(k)

print(dict["банан"])

dict["банан"] = "зеленый"
print(dict)

del(dict["банан"])
print(dict)