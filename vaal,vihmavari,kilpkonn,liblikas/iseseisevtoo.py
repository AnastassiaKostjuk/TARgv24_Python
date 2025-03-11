from tkinter import *
from tkinter import filedialog, messagebox
import smtplib
import ssl
from email.message import EmailMessage

def lisa():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Fail valitud", f"Fail {file_path} on valitud.")

def lisapilt():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Fail valitud", f"Fail {file_path} on valitud manusena.")

def saada():
    email = entry_email.get()
    teema = entry_teema.get()
    kiri = entry_kiri.get("1.0", END)

    if email and teema and kiri:
        try:
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "anastassia.kostjuk@gmail.com"
            password = "otxo rlfs dndx wdmj"
            context = ssl.create_default_context()

            msg = EmailMessage()
            msg.set_content(kiri)
            msg['Subject'] = teema
            msg['From'] = sender_email
            msg['To'] = email

            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.send_message(msg)
                messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
        except Exception as e:
            messagebox.showerror("Tekkis viga!", str(e))

def aken():
    aken = Tk()
    aken.geometry("700x500")
    aken.resizable(False, False)
    aken.title("E-kirja saatmine")
    aken.configure(bg="#2E3440")

    f1 = Frame(aken, width=700, height=500, bg="#2E3440")
    f1.pack(fill=BOTH, expand=True)

    # Заголовок
    lbl_title = Label(f1, text="E-KIRJA SAATMINE", font=("Helvetica", 20, "bold"), fg="#ECEFF4", bg="#2E3440")
    lbl_title.grid(row=0, column=0, columnspan=2, pady=20)

    # Поле для ввода email
    lbl_email = Label(f1, text="EMAIL:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    global entry_email
    entry_email = Entry(f1, font=("Helvetica", 14), width=30, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    # Поле для ввода темы
    lbl_teema = Label(f1, text="TEEMA:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_teema.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    global entry_teema
    entry_teema = Entry(f1, font=("Helvetica", 14), width=30, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_teema.grid(row=2, column=1, padx=10, pady=10)

    # Кнопка для добавления файла
    lbl_lisa = Label(f1, text="LISA FAIL:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_lisa.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    global entry_lisa
    entry_lisa = Button(f1, text="Vali fail", font=("Helvetica", 14), width=15, bg="#5E81AC", fg="#ECEFF4", command=lisa)
    entry_lisa.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Поле для ввода текста письма
    lbl_kiri = Label(f1, text="KIRI:", font=("Helvetica", 14), fg="#ECEFF4", bg="#2E3440")
    lbl_kiri.grid(row=4, column=0, padx=10, pady=10, sticky="ne")
    global entry_kiri
    entry_kiri = Text(f1, font=("Helvetica", 14), width=40, height=5, bg="#4C566A", fg="#ECEFF4", insertbackground="white")
    entry_kiri.grid(row=4, column=1, padx=10, pady=10)

    # Кнопка для добавления изображения
    btn_lisa_pilt = Button(f1, text="LISA PILT", font=("Helvetica", 14), bg="#5E81AC", fg="#ECEFF4", command=lisapilt)
    btn_lisa_pilt.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    # Кнопка для отправки письма
    btn_saada = Button(f1, text="SAADA KIRI", font=("Helvetica", 14), bg="#A3BE8C", fg="#2E3440", command=saada)
    btn_saada.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    aken.mainloop()

aken()