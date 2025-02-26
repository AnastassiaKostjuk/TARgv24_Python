from tkinter import *
from tkinter import filedialog, messagebox
import smtplib
import ssl
from email.message import EmailMessage
from gtts import *

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
            kellele = email  # Используем email из поля ввода
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "anastassia.kostjuk@gmail.com"
            password = ""  # Используйте пароль приложения здесь

            context = ssl.create_default_context()
            msg = EmailMessage()
            msg.set_content(kiri)
            msg['Subject'] = teema  # Тема из поля ввода
            msg['From'] = sender_email
            msg['To'] = kellele

            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.send_message(msg)

            messagebox.showinfo("Kiri saadetud", "Kiri on edukalt saadetud!")
        except Exception as e:
            messagebox.showerror("Viga", f"Tekkis viga: {e}")
    else:
        messagebox.showwarning("Viga", "Palun täitke kõik väljad.")

def aken():
    aken = Tk()
    aken.geometry("650x360")
    aken.resizable(False, False)
    aken.title("E-kirja saatmine")

    f1 = Frame(aken, width=650, height=360, bg="lightgrey")
    f1.pack(fill=BOTH, expand=True)

    lbl_email = Label(f1, text="EMAIL:", font="Calibri 14", fg="white", bg="green")
    lbl_email.grid(row=0, column=0, padx=10, pady=10)
    global entry_email
    entry_email = Entry(f1, font="Calibri 14", width=30, bg="lightgreen")
    entry_email.grid(row=0, column=1, padx=10, pady=10)

    lbl_teema = Label(f1, text="TEEMA:", font="Calibri 14", fg="white", bg="green")
    lbl_teema.grid(row=1, column=0, padx=10, pady=10)
    global entry_teema
    entry_teema = Entry(f1, font="Calibri 14", width=30, bg="lightgreen")
    entry_teema.grid(row=1, column=1, padx=10, pady=10)

    lbl_lisa = Label(f1, text="LISA:", font="Calibri 14", fg="white", bg="green")
    lbl_lisa.grid(row=2, column=0, padx=10, pady=10)
    global entry_lisa
    entry_lisa = Button(f1,text="...", font="Calibri 14", width=30, bg="lightgreen",command=lisa)
    entry_lisa.grid(row=2, column=1, padx=10, pady=10)
    

    lbl_kiri = Label(f1, text="KIRI:", font="Calibri 14", fg="white", bg="green")
    lbl_kiri.grid(row=3, column=0, padx=10, pady=10)
    global entry_kiri
    entry_kiri = Text(f1, font="Calibri 14", width=30, height=5, bg="lightgreen")
    entry_kiri.grid(row=3, column=1, padx=10, pady=10)

    btn_lisa_pilt = Button(f1, text="LISA PILT", font="Calibri 14", fg="green", command=lisapilt)
    btn_lisa_pilt.grid(row=4, column=0, padx=10, pady=10)

    btn_saada = Button(f1, text="SAADA", font="Calibri 14", fg="green", command=saada)
    btn_saada.grid(row=4, column=1, padx=10, pady=10)

    aken.mainloop()

aken()