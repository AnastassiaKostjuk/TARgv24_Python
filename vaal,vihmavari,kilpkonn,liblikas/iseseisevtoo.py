# Импортируем необходимые библиотеки
from tkinter import *  # Библиотека для создания графического интерфейса
from tkinter import filedialog, messagebox  # Модули для работы с файлами и всплывающими окнами
import smtplib  # Библиотека для отправки email через SMTP
import ssl  # Для безопасного соединения с SMTP-сервером
from email.message import EmailMessage  # Для создания email-сообщений
from email.mime.base import MIMEBase  # Для работы с вложениями
from email import encoders  # Для кодирования вложений
from PIL import Image  # Библиотека Pillow для работы с изображениями

# Глобальная переменная для хранения пути к выбранному файлу
file_path = None

# Функция для выбора файла
def lisa():
    global file_path  # Используем глобальную переменную file_path
    file_path = filedialog.askopenfilename()  # Открываем диалог выбора файла
    if file_path:  # Если файл выбран
        messagebox.showinfo("Fail valitud", f"Fail {file_path} on valitud.")  # Показываем сообщение об успешном выборе

# Функция для отправки письма
def saada():
    global file_path  # Используем глобальную переменную file_path
    email = entry_email.get()  # Получаем email получателя из поля ввода
    teema = entry_teema.get()  # Получаем тему письма из поля ввода
    kiri = entry_kiri.get("1.0", END)  # Получаем текст письма из текстового поля

    # Проверяем, что все поля заполнены
    if email and teema and kiri:
        try:
            # Настройки SMTP-сервера (для Gmail)
            smtp_server = "smtp.gmail.com"  # Адрес SMTP-сервера Gmail
            port = 587  # Порт для SMTP
            sender_email = "anastassia.kostjuk@gmail.com"  # Ваш email (отправитель)
            password = "otxo rlfs dndx wdmj"  # Ваш пароль (или пароль приложения)
            context = ssl.create_default_context()  # Создаем безопасное соединение

            # Создаем email-сообщение
            msg = EmailMessage()
            msg.set_content(kiri)  # Устанавливаем текст письма
            msg['Subject'] = teema  # Устанавливаем тему письма
            msg['From'] = sender_email  # Устанавливаем отправителя
            msg['To'] = email  # Устанавливаем получателя

            # Если файл выбран, добавляем его как вложение
            if file_path:
                with open(file_path, "rb") as file:  # Открываем файл в бинарном режиме
                    file_data = file.read()  # Читаем содержимое файла
                    file_name = file_path.split("/")[-1]  # Получаем имя файла из пути

                # Определяем тип файла (изображение или нет)
                try:
                    # Пытаемся открыть файл как изображение с помощью Pillow
                    with Image.open(file_path) as img:
                        img.verify()  # Проверяем, что это изображение
                    maintype = "image"  # Устанавливаем основной тип как "image"
                    subtype = Image.MIME[img.format]  # Получаем MIME-тип изображения
                except Exception:
                    # Если это не изображение, используем общий тип
                    maintype = "application"
                    subtype = "octet-stream"

                # Добавляем вложение к письму
                msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

            # Отправляем письмо через SMTP-сервер
            with smtplib.SMTP(smtp_server, port) as server:  # Подключаемся к SMTP-серверу
                server.starttls(context=context)  # Включаем шифрование
                server.login(sender_email, password)  # Авторизуемся на сервере
                server.send_message(msg)  # Отправляем письмо
                messagebox.showinfo("Informatsioon", "Kiri oli saadetud")  # Показываем сообщение об успешной отправке

        except Exception as e:  # Если произошла ошибка
            messagebox.showerror("Tekkis viga!", str(e))  # Показываем сообщение об ошибке

# Функция для создания графического интерфейса
def aken():
    aken = Tk()  # Создаем главное окно
    aken.geometry("700x500")  # Устанавливаем размер окна
    aken.resizable(False, False)  # Запрещаем изменение размера окна
    aken.title("E-kirja saatmine")  # Устанавливаем заголовок окна
    aken.configure(bg="#2E3440")  # Устанавливаем цвет фона окна

    # Создаем фрейм для размещения элементов интерфейса
    f1 = Frame(aken, width=700, height=500, bg="#2E3440")
    f1.pack(fill=BOTH, expand=True)  # Размещаем фрейм в окне

    # Заголовок окна
    lbl_title = Label(f1, text="E-KIRJA SAATMINE", font=("Helvetica", 20, "bold"), fg="#ECEFF4", bg="#2E3440")
    lbl_title.grid(row=0, column=0, columnspan=2, pady=20)  # Размещаем заголовок в фрейме

    # Поле для ввода email
    lbl_email = Label(f1, text="EMAIL:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Размещаем текст "EMAIL"
    global entry_email
    entry_email = Entry(f1, font=("Helvetica", 14), width=30, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_email.grid(row=1, column=1, padx=10, pady=10)  # Размещаем поле для ввода email

    # Поле для ввода темы
    lbl_teema = Label(f1, text="TEEMA:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_teema.grid(row=2, column=0, padx=10, pady=10, sticky="e")  # Размещаем текст "TEEMA"
    global entry_teema
    entry_teema = Entry(f1, font=("Helvetica", 14), width=30, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_teema.grid(row=2, column=1, padx=10, pady=10)  # Размещаем поле для ввода темы

    # Кнопка для добавления файла
    lbl_lisa = Label(f1, text="LISA FAIL:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_lisa.grid(row=3, column=0, padx=10, pady=10, sticky="e")  # Размещаем текст "LISA FAIL"
    global entry_lisa
    entry_lisa = Button(f1, text="Vali fail", font=("Helvetica", 14), width=15, bg="#5E81AC", fg="#ECEFF4", command=lisa)
    entry_lisa.grid(row=3, column=1, padx=10, pady=10, sticky="w")  # Размещаем кнопку для выбора файла

    # Поле для ввода текста письма
    lbl_kiri = Label(f1, text="KIRI:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_kiri.grid(row=4, column=0, padx=10, pady=10, sticky="ne")  # Размещаем текст "KIRI"
    global entry_kiri
    entry_kiri = Text(f1, font=("Helvetica", 14), width=40, height=5, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_kiri.grid(row=4, column=1, padx=10, pady=10)  # Размещаем текстовое поле для ввода письма

    # Кнопка для отправки письма
    btn_saada = Button(f1, text="SAADA KIRI", font=("Helvetica", 14), bg="#A3BE8C", fg="#2E3440", command=saada)
    btn_saada.grid(row=5, column=1, padx=10, pady=10, sticky="w")  # Размещаем кнопку для отправки письма

    aken.mainloop()  # Запускаем главный цикл обработки событий

# Запуск программы
aken()