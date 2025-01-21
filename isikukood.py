ikoodid = []
arvud = []

while True:
    # Запрашиваем личный код
    personal_code = input("Введите личный код (или 'stop' для завершения): ")
    if personal_code.lower() == 'stop':
        break

    # Проверяем длину кода
    if len(personal_code) != 11 or not personal_code.isdigit():
        print("Количество цифр неверное. Попробуйте снова.")
        arvud.append(personal_code)
        continue

    # Проверяем первый символ (пол)
    gender = int(personal_code[0])
    if gender not in [1, 2, 3, 4, 5, 6]:
        print("Первый символ неверный. Попробуйте снова.")
        arvud.append(personal_code)
        continue

    # Определяем год рождения
    if gender in [1, 2]:
        year_prefix = 18
    elif gender in [3, 4]:
        year_prefix = 19
    elif gender in [5, 6]:
        year_prefix = 20

    year = year_prefix * 100 + int(personal_code[1:3])
    month = int(personal_code[3:5])
    day = int(personal_code[5:7])

    # Проверяем дату рождения
    if not (1 <= month <= 12 and 1 <= day <= 31):  # Упрощенная проверка на дату
        print("Дата рождения неверная. Попробуйте снова.")
        arvud.append(personal_code)
        continue

    # Определяем место рождения
    hospital_number = int(personal_code[7:10])
    if 1 <= hospital_number <= 10:
        hospital = "Kuressaare Haigla"
    elif 11 <= hospital_number <= 19:
        hospital = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= hospital_number <= 150:
        hospital = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusмаja(Tallinn)"
    elif 151 <= hospital_number <=160:
        hospital= "Keila haigla"
    elif 161 <= hospital_number <=220:
        hospital= "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"
    elif 221 <= hospital_number <= 270:
        hospital = "Ida-Viru Keskhaiglа (Kohtla-Jarve, endine Jõhvi)"
    elif 271 <= hospital_number <= 370:
        hospital = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haiglа"
    elif 371 <= hospital_number <= 420:
        hospital = "Narva Haiglа"
    elif 421 <= hospital_number <= 470:
        hospital = "Pärnu Haiglа"
    elif 471 <= hospital_number <= 490:
        hospital = "Pelgulinna Sünnitusмаja (Tallinn), Haapsalu haiglа"
    elif 491 <= hospital_number <= 520:
        hospital = "Järvamaa Haiglа (Paide)"
    elif 521 <= hospital_number <= 570:
        hospital = "Rakvere, Tapa haiglа"
    elif 571 <= hospital_number <= 600:
        hospital = "Valga Haiglа"
    elif 601 <= hospital_number <= 650:
        hospital = "Viljandi Haiglа"
    elif 651 <= hospital_number <= 700:
        hospital = "Lõuna-Eesti Haigla (Võru), Põlva Haiglа"
    else:
        hospital = "Неизвестный регион"

    # Проверяем контрольный номер
    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum_1 = sum(int(personal_code[i]) * weights_1[i] for i in range(10))
    remainder = sum_1 % 11

    if remainder == 10:
        sum_2 = sum(int(personal_code[i]) * weights_2[i] for i in range(10))
        remainder = sum_2 % 11

    if remainder == 10:
        remainder = 0

    if remainder != int(personal_code[-1]):
        print("Контрольный номер неверный. Попробуйте снова.")
        arvud.append(personal_code)
        continue

    # Определяем пол
    if gender in [1, 3, 5]:
        gender_str = "мужчина"
    else:
        gender_str = "женщина"

    # Форматируем дату рождения
    birth_date = f"{day:02}.{month:02}.{year}"

    print(f"Это {gender_str}, его/ее день рождения {birth_date} и место рождения {hospital}.")
    ikoodid.append(personal_code)

# Сортируем списки
women = []
men = []

for code in ikoodid:
    if int(code[0]) % 2 == 0:  # Женщины: 2, 4, 6
        women.append(code)
    else:  # Мужчины: 1, 3, 5
        men.append(code)

ikoodid = women + men

arvud.sort()


# Выводим результаты
print("Список правильных личных кодов (ikoodid):", ikoodid)
print("Список неверных кодов (arvud):", arvud)

