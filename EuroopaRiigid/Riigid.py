from tkinter import *
from tkinter import messagebox, simpledialog
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
                        messagebox.showerror("Ошибка", f"Неправильный формат строки: {line}")
    except FileNotFoundError:
        messagebox.showinfo("Информация", f"Файл '{f}' не найден. Создан новый словарь.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при чтении файла: {e}")
    return riik_pealinn, pealinn_riik, riigid, pealinnad

# Функция для отображения словаря
def display_dictionary():
    text.delete(1.0, END)  # Очистка текстового поля
    for k, v in riik_pealinn.items():
        text.insert(END, f"{k} - {v}\n")

# Функция для отображения страны по столице
def display_country_by_capital():
    capital = simpledialog.askstring("Ввод", "Введите столицу:")
    if capital:
        if capital in pealinnad:
            messagebox.showinfo("Результат", f"Страна: {pealinn_riik[capital]}\nСтолица: {capital}")
        else:
            messagebox.showwarning("Ошибка", "Такой столицы нет в словаре.")

# Функция для отображения столицы по стране
def display_capital_by_country():
    country = simpledialog.askstring("Ввод", "Введите страну:")
    if country:
        if country in riigid:
            messagebox.showinfo("Результат", f"Страна: {country}\nСтолица: {riik_pealinn[country]}")
        else:
            messagebox.showwarning("Ошибка", "Такой страны нет в словаре.")

# Функция для добавления новых данных
def add_data():
    country = simpledialog.askstring("Ввод", "Введите страну:")
    if country:
        capital = simpledialog.askstring("Ввод", "Введите столицу:")
        if capital:
            if country in riigid or capital in pealinnad:
                messagebox.showwarning("Ошибка", "Такие данные уже есть в словаре!")
            else:
                with open("EuroopaRiigid/riigid_pealinnad.txt", 'a', encoding='utf-8') as file:
                    file.write(f"{country}-{capital}\n")
                riik_pealinn[country] = capital
                pealinn_riik[capital] = country
                riigid.append(country)
                pealinnad.append(capital)
                messagebox.showinfo("Успех", "Данные добавлены.")

# Функция для обновления данных
def update_data():
    choice = simpledialog.askstring("Ввод", "Что вы хотите обновить?\n1 - Страну\n2 - Столицу")
    if choice == '1':
        old_country = simpledialog.askstring("Ввод", "Введите старую страну:")
        if old_country in riigid:
            new_country = simpledialog.askstring("Ввод", "Введите новую страну:")
            if new_country:
                capital = riik_pealinn.pop(old_country)
                riik_pealinn[new_country] = capital
                pealinn_riik[capital] = new_country
                riigid.remove(old_country)
                riigid.append(new_country)
                messagebox.showinfo("Успех", "Страна обновлена.")
        else:
            messagebox.showwarning("Ошибка", "Такой страны нет в словаре.")
    elif choice == '2':
        old_capital = simpledialog.askstring("Ввод", "Введите старую столицу:")
        if old_capital in pealinnad:
            new_capital = simpledialog.askstring("Ввод", "Введите новую столицу:")
            if new_capital:
                country = pealinn_riik.pop(old_capital)
                pealinnad.remove(old_capital)
                pealinnad.append(new_capital)
                riik_pealinn[country] = new_capital
                pealinn_riik[new_capital] = country
                messagebox.showinfo("Успех", "Столица обновлена.")
        else:
            messagebox.showwarning("Ошибка", "Такой столицы нет в словаре.")
    else:
        messagebox.showwarning("Ошибка", "Выберите 1 или 2!")

# Функция для проверки знаний
def knowledge_test():
    correct = 0
    total = 0

    while True:
        question_type = choice(["country", "capital"])
        if question_type == "country":
            country = choice(riigid)
            answer = simpledialog.askstring("Тест", f"{country}: столица - ")
            if answer.upper() == "X":
                break
            elif answer == riik_pealinn[country]:
                correct += 1
                messagebox.showinfo("Результат", "Правильно! Молодец!")
            else:
                messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {riik_pealinn[country]}")
        else:
            capital = choice(pealinnad)
            answer = simpledialog.askstring("Тест", f"{capital}: страна - ")
            if answer.upper() == "X":
                break
            elif answer == pealinn_riik[capital]:
                correct += 1
                messagebox.showinfo("Результат", "Правильно! Молодец!")
            else:
                messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {pealinn_riik[capital]}")
        total += 1
    if total > 0:
        result = correct * 100 / total
        messagebox.showinfo("Итог", f"У вас {correct} правильных ответов. Результат: {result:.2f}%")

# Создание графического интерфейса
root = Tk()
root.title("Словарь стран и столиц")
root.geometry("500x400")

# Текстовое поле для отображения словаря
text = Text(root, wrap=WORD, width=60, height=15)
text.pack(pady=10)

# Кнопки для выполнения функций
Button(root, text="Показать словарь", command=display_dictionary).pack(pady=5)
Button(root, text="Показать страну по столице", command=display_country_by_capital).pack(pady=5)
Button(root, text="Показать столицу по стране", command=display_capital_by_country).pack(pady=5)
Button(root, text="Добавить данные", command=add_data).pack(pady=5)
Button(root, text="Обновить данные", command=update_data).pack(pady=5)
Button(root, text="Проверить знания", command=knowledge_test).pack(pady=5)
Button(root, text="Выход", command=root.quit).pack(pady=5)

# Загрузка данных при запуске программы
load_data_from_file("EuroopaRiigid/riigid_pealinnad.txt")

# Запуск основного цикла
root.mainloop()