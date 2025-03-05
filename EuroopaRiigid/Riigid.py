from random import *
from gtts import *

# Глобальные переменные для хранения данных
riik_pealinn = {}  # словарь: страна -> столица
pealinn_riik = {}  # словарь: столица -> страна
riigid = []        # список стран
pealinnad = []     # список столиц

# Функция для загрузки данных из файла
def failist_to_dict(f:str):
    file=open(f,'r',encoding="utf-8")
    for line in file:
        k,v=line.strip().split('-',1) #k-võti, v-väärtus
        riik_pealinn[k]=v #täidame riik_pealinn
        pealinn_riik[v]=k #täidame pealinn_riik
        riigid.append(k)
        pealinnad.append(v)
    file.close()
    return riik_pealinn,pealinn_riik,riigid,pealinnad

# Функция для поиска страны по столице
def kuvada_pealinna_riik():
    pealinn = input("Введите название столицы (или X для выхода): ")
    if pealinn.upper() == "X":
        return
    elif pealinn in pealinn_riik:
        print(f"Страна с столицей {pealinn} - {pealinn_riik[pealinn]}")
    else:
        print("Такой столицы нет в словаре.")

# Функция для поиска столицы по стране
def kuvada_riigi_pealinn():
    riik = input("Введите название страны (или X для выхода): ")
    if riik.upper() == "X":
        return
    elif riik in riik_pealinn:
        print(f"Столица страны {riik} - {riik_pealinn[riik]}")
    else:
        print("Такой страны нет в словаре.")

# Функция для добавления новых данных
def lisamine(f: str):
    riik = input("Введите название страны: ")
    pealinn = input("Введите столицу страны: ")
    if riik in riigid or pealinn in pealinnad:
        print("Эти данные уже есть в словаре.")
    else:
        with open(f, 'a', encoding="utf-8") as file:
            file.write(f"{riik}-{pealinn}\n")
        riik_pealinn[riik] = pealinn
        pealinn_riik[pealinn] = riik
        riigid.append(riik)
        pealinnad.append(pealinn)
        print("Данные успешно добавлены.")

# Функция для удаления страны и столицы
def kustuta_riik(f: str):
    riik = input("Введите название страны, которую хотите удалить: ")
    if riik in riik_pealinn:
        pealinn = riik_pealinn.pop(riik)
        pealinn_riik.pop(pealinn)
        riigid.remove(riik)
        with open(f, 'w', encoding="utf-8") as file:
            for k, v in riik_pealinn.items():
                file.write(f"{k}-{v}\n")
        print(f"Страна '{riik}' и её столица '{pealinn}' удалены.")
    else:
        print("Такой страны нет в словаре.")

# Функция для сортировки стран и столиц
def sorteeri_riigid():
    sorted_riigid = sorted(riik_pealinn.items(), key=lambda x: x[0])
    print("\nОтсортированные страны и их столицы:")
    for riik, pealinn in sorted_riigid:
        print(f"{riik} - {pealinn}")

# Функция для экспорта данных в файл
def ekspordi_faili(f: str):
    with open(f, 'w', encoding="utf-8") as file:
        for riik, pealinn in riik_pealinn.items():
            file.write(f"{riik}-{pealinn}\n")
    print(f"Данные экспортированы в файл {f}.")

# Функция для тестирования знаний
def kontrolltest():
    count = 0  # количество правильных ответов
    total = 0  # общее количество вопросов
    print("Начинаем тест (для выхода нажмите X).")
    while True:
        # Выбираем случайный вопрос
        if choice(["riik", "pealinn"]) == "riik":
            riik = choice(riigid)
            vastus = input(f"Какая столица у страны {riik}? ")
            if vastus.upper() == "X":
                break
            elif vastus == riik_pealinn[riik]:
                count += 1
                print("Правильный ответ!")
            else:
                print(f"Неправильный ответ. Правильная столица: {riik_pealinn[riik]}")
        else:
            pealinn = choice(pealinnad)
            vastus = input(f"Какая страна имеет столицу {pealinn}? ")
            if vastus.upper() == "X":
                break
            elif vastus == pealinn_riik[pealinn]:
                count += 1
                print("Правильный ответ!")
            else:
                print(f"Неправильный ответ. Правильная страна: {pealinn_riik[pealinn]}")
        total += 1

    if total > 0:
        print(f"Ваш результат: {count} из {total}. Процент правильных ответов: {count / total * 100:.2f}%")