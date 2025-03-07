import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, scrolledtext  # Добавляем scrolledtext для прокрутки
from PIL import Image, ImageTk  # Библиотека для работы с изображениями

# Словарь для русского алфавита
russian_alphabet = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9,
    'и': 1, 'й': 2, 'к': 3, 'л': 4, 'м': 5, 'н': 6, 'о': 7, 'п': 8, 'р': 9,
    'с': 1, 'т': 2, 'у': 3, 'ф': 4, 'х': 5, 'ц': 6, 'ч': 7, 'ш': 8, 'щ': 9,
    'ъ': 1, 'ы': 2, 'ь': 3, 'э': 4, 'ю': 5, 'я': 6
}

# Словарь для латинского алфавита
latin_alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
    's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
}

# Функция для проверки, содержит ли имя одновременно русские и латинские буквы
def is_mixed_language(name):
    has_russian = any(char in russian_alphabet for char in name)
    has_latin = any(char in latin_alphabet for char in name)
    return has_russian and has_latin

# Функция для расчета числа имени
def calculate_name_number(name, alphabet):
    total = 0
    for char in name.lower():
        if char in alphabet:
            total += alphabet[char]
    # Сводим сумму к однозначному числу
    while total >= 10:
        total = sum(map(int, str(total)))
    return total

# Функция для отображения пояснения в новом окне
def show_meaning(number):
    # Открытие нового окна
    new_window = Toplevel(root)
    new_window.geometry("600x400")  # Увеличиваем размер окна
    new_window.title(f"Значение числа {number}")

    # Попытка прочитать значение из текстового файла
    try:
        with open('Numeroloogia_Nimearv/numbrid.txt', 'r', encoding="utf-8") as file:
            meanings = file.readlines()
        
        # Ищем описание для числа
        description = "Описание не найдено."
        for line in meanings:
            try:
                num, meaning = line.split(":", 1)
                if int(num) == number:
                    description = meaning.strip()
                    break
            except ValueError:
                continue  # Пропускаем строки, которые не удалось разобрать

        # Создаем текстовое поле с прокруткой
        text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
        text_area.insert(tk.INSERT, description)  # Вставляем текст
        text_area.configure(state='disabled')  # Запрещаем редактирование
        text_area.pack(padx=10, pady=10)

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл с описаниями не найден!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для обработки нажатия кнопки
def calculate():
    name = entry.get().strip()
    if not name:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите имя.")
        return

    # Проверка на смешанные буквы (латиница и кириллица)
    if is_mixed_language(name):
        messagebox.showwarning("Ошибка", "Имя не должно содержать и латинские, и русские буквы одновременно.")
        return

    # Определение языка и выбор алфавита
    if any(char in russian_alphabet for char in name):
        alphabet = russian_alphabet
    elif any(char in latin_alphabet for char in name):
        alphabet = latin_alphabet
    else:
        messagebox.showwarning("Ошибка", "Имя должно содержать хотя бы одну букву.")
        return

    # Расчет числа имени
    name_number = calculate_name_number(name, alphabet)

    # Вывод результата
    result_label.config(text=f"Число вашего имени: {name_number}")

    # Открытие нового окна с объяснением
    show_meaning(name_number)

# Создание графического интерфейса
root = tk.Tk()
root.geometry("650x360")
root.resizable(False, False)
root.title("Расчет числа имени")

# Загрузка фонового изображения
try:
    bg_image = Image.open("Numeroloogia_Nimearv/246.jpg")  # Укажите путь к вашему изображению
    bg_image = bg_image.resize((650, 360), Image.Resampling.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
    bg_image = ImageTk.PhotoImage(bg_image)
except Exception as e:
    print(f"Ошибка загрузки изображения: {e}")
    bg_image = None

# Создание Canvas для отображения фонового изображения
canvas = tk.Canvas(root, width=650, height=360)
canvas.pack(fill="both", expand=True)

# Установка фонового изображения
if bg_image:
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
else:
    # Если изображение не загружено, устанавливаем белый фон
    canvas.create_rectangle(0, 0, 650, 360, fill="white")

# Создание Frame поверх Canvas для ввода данных
frame = tk.Frame(root, bg="white", bd=2)  # Устанавливаем белый фон для Frame
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.6)

# Поле для ввода имени
label = tk.Label(frame, text="Введите ваше имя:", bg="white", fg="maroon", font=("Arial", 14))
label.place(relx=0.5, rely=0.3, anchor="center")

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.place(relx=0.5, rely=0.4, anchor="center")

# Кнопка для расчета
button = tk.Button(frame, text="Рассчитать", command=calculate, bg="#ccccff", fg="white", font=("Arial", 12))
button.place(relx=0.5, rely=0.55, anchor="center")

# Поле для вывода результата
result_label = tk.Label(frame, text="Число вашего имени: ", bg="white", fg="maroon", font=("Arial", 14))
result_label.place(relx=0.5, rely=0.7, anchor="center")

# Запуск основного цикла
root.mainloop() 