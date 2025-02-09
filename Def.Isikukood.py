def vvod_i_proverka_koda():
    """Запрашивает и проверяет личный код, возвращает код или None, если ввод 'stop'."""
    while True:
        kod = input("Введите личный код (или 'stop' для завершения): ")
        if kod.lower() == 'stop':
            return None  # Пользователь хочет завершить ввод
        if not proverka_dlina_koda(kod):
            print("Количество цифр неверное. Попробуйте снова.")
            continue
        if not proverka_pervyi_simvol(kod):
            print("Первый символ неверный. Попробуйте снова.")
            continue
        if not proverka_data_rozhdeniya(kod):
            print("Дата рождения неверная. Попробуйте снова.")
            continue
        if not proverka_kontrolny_nomer(kod):
            print("Контрольный номер неверный. Попробуйте снова.")
            continue
        return kod  # Код прошел все проверки, возвращаем его

def proverka_dlina_koda(kod):
    """Проверяет длину кода (11 символов) и состоит ли он из цифр."""
    return len(kod) == 11 and kod.isdigit()

def proverka_pervyi_simvol(kod):
    """Проверяет первый символ кода (пол)."""
    return int(kod[0]) in [1, 2, 3, 4, 5, 6]

def proverka_data_rozhdeniya(kod):
    """Проверяет корректность даты рождения (упрощенно)."""
    pol = int(kod[0])
    if pol in [1, 2]:
        god_prefix = 18
    elif pol in [3, 4]:
        god_prefix = 19
    elif pol in [5, 6]:
        god_prefix = 20
    god = god_prefix * 100 + int(kod[1:3])
    mesyats = int(kod[3:5])
    den = int(kod[5:7])
    return 1 <= mesyats <= 12 and 1 <= den <= 31  # Упрощенная проверка

def proverka_kontrolny_nomer(kod):
    """Проверяет контрольный номер."""
    vesa_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    vesa_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    summa_1 = sum(int(kod[i]) * vesa_1[i] for i in range(10))
    ostatok = summa_1 % 11
    if ostatok == 10:
        summa_2 = sum(int(kod[i]) * vesa_2[i] for i in range(10))
        ostatok = summa_2 % 11
    if ostatok == 10:
        ostatok = 0
    return ostatok == int(kod[-1])

def opredelenie_pola(kod):
    """Определяет пол по первому символу кода."""
    if int(kod[0]) in [1, 3, 5]:
        return "мужчина"
    else:
        return "женщина"

def opredelenie_mesta_rozhdeniya(kod):
    """Определяет место рождения по номеру роддома."""
    nomer_roddoma = int(kod[7:10])
    if 1 <= nomer_roddoma <= 10:
        mesto_rozhdeniya = "Kuressaare Haigla"
    elif 11 <= nomer_roddoma <= 19:
        mesto_rozhdeniya = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= nomer_roddoma <= 150:
        mesto_rozhdeniya = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja(Tallinn)"
    elif 151 <= nomer_roddoma <= 160:
        mesto_rozhdeniya = "Keila haigla"
    elif 161 <= nomer_roddoma <= 220:
        mesto_rozhdeniya = "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"
    elif 221 <= nomer_roddoma <= 270:
        mesto_rozhdeniya = "Ida-Viru Keskhaigla (Kohtla-Jarve, endine Jõhvi)"
    elif 271 <= nomer_roddoma <= 370:
        mesto_rozhdeniya = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= nomer_roddoma <= 420:
        mesto_rozhdeniya = "Narva Haigla"
    elif 421 <= nomer_roddoma <= 470:
        mesto_rozhdeniya = "Pärnu Haigla"
    elif 471 <= nomer_roddoma <= 490:
        mesto_rozhdeniya = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491 <= nomer_roddoma <= 520:
        mesto_rozhdeniya = "Järvamaa Haigla (Paide)"
    elif 521 <= nomer_roddoma <= 570:
        mesto_rozhdeniya = "Rakvere, Tapa haigla"
    elif 571 <= nomer_roddoma <= 600:
        mesto_rozhdeniya = "Valga Haigla"
    elif 601 <= nomer_roddoma <= 650:
        mesto_rozhdeniya = "Viljandi Haigla"
    elif 651 <= nomer_roddoma <= 700:
        mesto_rozhdeniya = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        mesto_rozhdeniya = "Неизвестный регион"
    return mesto_rozhdeniya

def format_data_rozhdeniya(kod):
    """Форматирует дату рождения в строку."""
    pol = int(kod[0])
    if pol in [1, 2]:
        god_prefix = 18
    elif pol in [3, 4]:
        god_prefix = 19
    elif pol in [5, 6]:
        god_prefix = 20
    god = god_prefix * 100 + int(kod[1:3])
    mesyats = int(kod[3:5])
    den = int(kod[5:7])
    return f"{den:02}.{mesyats:02}.{god}"

# Основная часть программы
ikoodid = []
arvud = []

while True:
    kod = vvod_i_proverka_koda()
    if kod is None:
        break  # Пользователь завершил ввод

    pol = opredelenie_pola(kod)
    mesto_rozhdeniya = opredelenie_mesta_rozhdeniya(kod)
    data_rozhdeniya = format_data_rozhdeniya(kod)

    print(f"Это {pol}, его/ее день рождения {data_rozhdeniya} и место рождения {mesto_rozhdeniya}.")
    ikoodid.append(kod)

# Сортировка по полу (женщины, потом мужчины)
naised = []
mehed = []
for kod in ikoodid:
    if int(kod[0]) % 2 == 0:
        naised.append(kod)
    else:
        mehed.append(kod)
ikoodid = naised + mehed

arvud.sort()  # Сортируем список неверных кодов

# Выводим результаты
print("Список правильных личных кодов (ikoodid):", ikoodid)
print("Список неверных кодов(arvud):", arvud)
