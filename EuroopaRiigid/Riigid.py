from random import choice

# Глобальные переменные для хранения данных
riik_pealinn = {}  # словарь {"Riik": "Pealinn"}
pealinn_riik = {}  # словарь {"Pealinn": "Riik"}
riigid = []        # список стран
pealinnad = []     # список столиц

# Функция для загрузки данных из файла
def load_data_from_file(f: str):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # Пропускаем пустые строки
                    try:
                        k, v = line.split('-')  # Разделяем по '-'
                        riik_pealinn[k] = v
                        pealinn_riik[v] = k
                        riigid.append(k)
                        pealinnad.append(v)
                    except ValueError:
                        print(f"Неправильный формат строки: {line}")
    except FileNotFoundError:
        print(f"Файл '{f}' не найден. Создан новый словарь.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return riik_pealinn, pealinn_riik, riigid, pealinnad

# Функция для отображения словаря
def display_dictionary():
    for k, v in riik_pealinn.items():
        print(f"{k} - {v}")
    return True

# Функция для отображения страны или столицы
def display_country_or_capital():
    while True:
        print("1 - Показать страну по столице\n2 - Показать столицу по стране\n3 - Выход")
        choice = input("Ваш выбор: ")
        print()
        if choice == '1':
            capital = input("Введите столицу (для выхода введите X): ")
            if capital.upper() == "X":
                break
            elif capital not in pealinnad:
                print("Такой столицы нет в словаре.")
                print()
            else:
                print(f"Страна: {pealinn_riik[capital]}\nСтолица: {capital}")
                print()
        elif choice == '2':
            country = input("Введите страну (для выхода введите X): ")
            if country.upper() == "X":
                break
            elif country not in riigid:
                print("Такой страны нет в словаре.")
                print()
            else:
                print(f"Страна: {country}\nСтолица: {riik_pealinn[country]}")
                print()
        elif choice == '3':
            break
        else:
            print("Выберите 1, 2 или 3!")
    return True

# Функция для добавления новых данных
def add_data(f: str):
    while True:
        try:
            country = input("Введите страну (для выхода введите X): ")
            if country.upper() == "X":
                break
            capital = input("Введите столицу: ")
            if country in riigid or capital in pealinnad:
                print("Такие данные уже есть в словаре!")
            else:
                with open(f, 'a', encoding='utf-8') as file:
                    file.write(f"{country}-{capital}\n")
                riik_pealinn[country] = capital
                pealinn_riik[capital] = country
                riigid.append(country)
                pealinnad.append(capital)
                print("Данные добавлены.")
                print()
        except Exception as e:
            print(f"Ошибка: {e}")
            print()

# Функция для обновления данных
def update_data(f: str):
    print("Что вы хотите обновить?\n1 - Страну\n2 - Столицу")
    try:
        choice = int(input("Ваш выбор: "))
        print()
    except ValueError:
        print("Выберите 1 или 2!")
        return
    if choice == 1:
        old_country = input("Введите старую страну: ")
        if old_country not in riigid:
            print("Такой страны нет в словаре.")
            print()
            return
        new_country = input("Введите новую страну: ")
        if new_country in riigid:
            print("Такая страна уже есть в словаре.")
            print()
            return
        capital = riik_pealinn.pop(old_country)
        riik_pealinn[new_country] = capital
        pealinn_riik[capital] = new_country
        riigid.remove(old_country)
        riigid.append(new_country)
        print("Страна обновлена.")
        print()
    elif choice == 2:
        old_capital = input("Введите старую столицу: ")
        if old_capital not in pealinnad:
            print("Такой столицы нет в словаре.")
            print()
            return
        new_capital = input("Введите новую столицу: ")
        if new_capital in pealinnad:
            print("Такая столица уже есть в словаре.")
            print()
            return
        country = pealinn_riik.pop(old_capital)
        pealinnad.remove(old_capital)
        pealinnad.append(new_capital)
        riik_pealinn[country] = new_capital
        pealinn_riik[new_capital] = country
        print("Столица обновлена.")
        print()
    else:
        print("Выберите 1 или 2!")
    with open(f, 'w', encoding='utf-8') as file:
        for country, capital in riik_pealinn.items():
            file.write(f"{country}-{capital}\n")

# Функция для проверки знаний
def knowledge_test():
    correct = 0
    total = 0
    print("Начинаем тест (для выхода введите X): ")
    while True:
        question_type = choice(["country", "capital"])
        if question_type == "country":
            country = choice(riigid)
            answer = input(f"{country}: столица - ")
            correct_answer = riik_pealinn[country]
            if answer.upper() == "X":
                break
            elif answer == correct_answer:
                correct += 1
                print("Правильно! Молодец!")
                print()
            else:
                print(f"Неправильно! Правильный ответ: {correct_answer}")
                print()
        else:
            capital = choice(pealinnad)
            answer = input(f"{capital}: страна - ")
            correct_answer = pealinn_riik[capital]
            if answer.upper() == "X":
                break
            elif answer == correct_answer:
                correct += 1
                print("Правильно! Молодец!")
                print()
            else:
                print(f"Неправильно! Правильный ответ: {correct_answer}")
                print()
        total += 1
    if total > 0:
        result = correct * 100 / total
        print(f"У вас {correct} правильных ответов. Результат: {result:.2f}%")
        print()

# Основная программа
def main():
    filename = ('EuroopaRiigid/riigid_pealinnad.txt') 
    riik_pealinn, pealinn_riik, riigid, pealinnad = load_data_from_file(filename)

    while True:
        print("Словарь стран и столиц! Что вы хотите сделать?\n1 - Показать словарь\n2 - Показать страну или столицу\n3 - Добавить данные\n4 - Обновить данные\n5 - Проверить знания\n6 - Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':
            print()
            display_dictionary()
            print()
        elif choice == '2':
            display_country_or_capital()
        elif choice == '3':
            add_data(filename)
        elif choice == '4':
            update_data(filename)
        elif choice == '5':
            knowledge_test()
        elif choice == '6':
            break
        else:
            print("Выберите 1, 2, 3, 4, 5 или 6!")

# Запуск программы
if __name__ == "__main__":
    main()