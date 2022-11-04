"""Работа со строками"""

print("""Привет
мир!
Hello
world!""")

print("Привет\nПривет\tПриветПривет")

text = "Salom"
print(text*5)

print(text[0])

print(text[0:3])

print(text.upper())

print(text.lower())

print(text.capitalize())

text1 = "Привет мир, куда-идешь"
print(text.split(" "))

spisok = ["a", "b", "c"]
print(",".join(spisok))


tekst = "      Salom        "
print(tekst.strip())

print(tekst.lstrip())

print(tekst.rstrip())

text2 = "ololololololol"
print(text2.replace("l", "o"))