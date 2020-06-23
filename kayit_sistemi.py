ogrenciler = {}

print(" ")
print("1. Öğrenci")

number = input("Öğrenci No: ")
name = input("Ad: ")
surname = input("Soyad: ")
phone = input("Telefon: ")

ogrenciler[number] = {
    "Adı": name,
    "Soyadı": surname,
    "Telefonu":phone
}

print(" ")
print("2. Öğrenci")

number = input("Öğrenci No: ")
name = input("Ad: ")
surname = input("Soyad: ")
phone = input("Telefon: ")

ogrenciler[number] = {
    "Adı": name,
    "Soyadı": surname,
    "Telefonu":phone
}

print(" ")
print("3. Öğrenci")

number = input("Öğrenci No: ")
name = input("Ad: ")
surname = input("Soyad: ")
phone = input("Telefon: ")

ogrenciler[number] = {
    "Adı": name,
    "Soyadı": surname,
    "Telefonu":phone
}


print(" ")
ogrenciNo = input("Öğrenci no: ")
ogrenci = ogrenciler[ogrenciNo]

print(" ")
print("Aradığınız öğrencinin;")
print(f"Adı: {ogrenci['Adı']}")
print(f"Soyadı: {ogrenci['Soyadı']}")
print(f"Telefonu ise: {ogrenci['Telefonu']}")
print(" ")
