
isiku_kood = input("Введите свой личный код: ")
kokku_mehed = 0
kokku_naised = 0
esimene_number = isiku_kood[0]
print(f"Первая цифра личного кода: {esimene_number}")

if esimene_number in [1, 3, 5, 7, 9]:
    kokku_mehed +=1
    print("Мужчина")

if esimene_number in [2, 4, 6, 8]:
    kokku_naised +=1
    print("Женщина")


