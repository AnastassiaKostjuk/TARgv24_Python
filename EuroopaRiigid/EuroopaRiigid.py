from random import *
from os import system
from gtts import *
import os
from random import choice

# Словари и списки для хранения данных
riik_pealinn = {}  # страна - столица
pealinn_riik = {}  # столица - страна
riigid = []  # список стран
pealinnad = []  # список столиц

# Загрузка данных из файла в словари
def failist_to_dict(f:str):
    try:
        with open(f, 'r', encoding="utf-8") as file:
            for line in file:
                k, v = line.strip().split('-')
                riik_pealinn[k] = v
                pealinn_riik[v] = k
                riigid.append(k)
                pealinnad.append(v)
        return riik_pealinn, pealinn_riik, riigid, pealinnad
    except FileNotFoundError:
        print(f"Ошибка: Файл '{f}' не найден. Убедитесь, что файл существует и путь указан правильно.")
        return {}, {}, [], []

# Функция для отображения всех стран и столиц
def sonastik():
    for k, v in riik_pealinn.items():
        print(f"{k} - {v}")

# Функция для поиска столицы по названию страны
def kuvada_riigi_pealinn():
    riik = input("Введите название страны (или X для выхода): ")
    if riik.upper() == "X":
        return
    elif riik in riik_pealinn:
        print(f"Столица страны {riik} - {riik_pealinn[riik]}")
    else:
        print("Такой страны нет в словаре.")

# Функция для поиска страны по названию столицы
def kuvada_pealinna_riik():
    pealinn = input("Введите название столицы (или X для выхода): ")
    if pealinn.upper() == "X":
        return
    elif pealinn in pealinn_riik:
        print(f"Страна с столицей {pealinn} - {pealinn_riik[pealinn]}")
    else:
        print("Такой столицы нет в словаре.")

# Функция для добавления новых данных в словарь
def lisamine(f:str):
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

# Функция для тестирования знаний пользователя
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

# Основное меню
def main():
    failist_to_dict("riigid_pealinnad.txt")  # Загружаем данные из файла
    while True:
        print("\n1. Показать страну по столице")
        print("2. Показать столицу по стране")
        print("3. Добавить новую страну и столицу")
        print("4. Начать тест")
        print("5. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            kuvada_pealinna_riik()
        elif choice == '2':
            kuvada_riigi_pealinn()
        elif choice == '3':
            lisamine("riigid_pealinnad.txt")
        elif choice == '4':
            kontrolltest()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()