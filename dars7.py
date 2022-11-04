lugat = {
    "Apple": {
        "a": ["iPhone 13 Pro Max", "1250$"],
        "b": ["MacBook Air M1", "16 000 000"],
        "c": ["MacBook Pro M2", "18 500 500"],
    },
    "Samsung": {
        "a": ["Galaxy Book2 Pro 360", "1,293$"],
        "b": ["Galaxy A73", "7 231 000"],
        "c": ["EcoBubble kir yuvish mashinasi", "9 430 000"],
    },
    "Huawei": {
        "a": ["HUAWEI P50 Pro", "12 500 000"],
        "b": ["Huawei P smart 2021", "9 000 000"],
        "c": ["Huawei nava 9", "10 900 000"],
    }
}
a = input("""Apple
Samsung
Huawei
: """)
b = a.lower()

if b == "apple":
    print("siz tanlagan tovarlar", lugat["Apple"])

    apple = input("Uzingizga kerakli bo'lgan bo'limni tanlang a,b,c : ")

    if apple.lower() == "a":
        print("siz tanlagan maxsulaot bu", lugat["Apple"]["a"][0], "uning narxi", lugat["Apple"]["a"][1])

    elif apple.lower() == "b":
        print("siz tanlagan maxsulaot bu", lugat["Apple"]["b"][0], "uning narxi", lugat["Apple"]["b"][1])

    elif apple.lower() == "c":
        print("siz tanlagan maxsulaot bu", lugat["Apple"]["c"][0], "uning narxi", lugat["Apple"]["c"][1])
    else:
        print("Xato")

elif b == "samsung":
    print(lugat["Samsung"])

    samsung = input("Uzingizga kerakli bo'lgan bo'limni tanlang a,b,c : ")

    if samsung.lower() == "a":
        print("siz tanlagan maxsulaot bu", lugat["Samsung"]["a"][0], "uning narxi", lugat["Samsung"]["a"][1] )
    elif samsung.lower() == "a":
        print("siz tanlagan maxsulaot bu", lugat["Samsung"]["b"][0], "uning narxi", lugat["Samsung"]["b"][1])
    elif samsung.lower() == "a":
        print("siz tanlagan maxsulaot bu", lugat["Samsung"]["c"][0], "uning narxi", lugat["Samsung"]["c"][1])
    else:
        print("xato")

elif b == "huawei".lower():
    print(lugat["Huawei"])

    huawei = input("Uzingizga kerakli bo'lgan bo'limni tanlang a,b,c : ")

    if huawei.lower() == "a":
        print("siz tanlagan maxsulaot bu", lugat["Huawei"]["a"][0], "uning narxi", lugat["Huawei"]["a"][1])
    elif huawei.lower() == "b":
        print("siz tanlagan maxsulaot bu", lugat["Huawei"]["b"][0], "uning narxi", lugat["Huawei"]["b"][1])
    elif huawei.lower() == "c":
        print("siz tanlagan maxsulaot bu", lugat["Huawei"]["c"][0], "uning narxi", lugat["Huawei"]["c"][1])
    else:
        print("xato")

else:
    print("XATO")

    