from tkinter import *
from PIL import Image,ImageTk


def Lahenda():
    pass

def Graafik():
    pass

def aken():
    aken=Tk()
    aken.geometry("650x260")
    aken.resizable(False,False)
    aken.title("Ruutvõrrand")
    pilt=Image.open("Math-Background.jpg")
    pilt2=pilt("650x260")
    bgPilt=ImageTk.PhotoImage(pilt2)

    labelBG=Label(aken,image=bgPilt)
    labelBG.place(x=0,y=0)

    f1=Frame(aken,width=650,height=260)
    f1.pack()
    lbl=Label(f1,text="Ruutvõrrandite lahendamine",font="Calibri 26",fg="green",bg="lightblue")
    lbl.pack(side=TOP)
    lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
    lbl_vastus.pack(side=BOTTOM)
    lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_a.pack(side=LEFT)
    x2=Label(f1,text="x**2+",font="Calibri 26",fg="green",padx=10)
    x2.pack(side=LEFT)
    lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_b.pack(side=LEFT)
    x=Label(f1,text="x+",font="Calibri 26",fg="green",bg="lightblue")
    x.pack(side=LEFT)
    lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_c.pack(side=LEFT)
    y=Label(f1,text="=0",font="Calibri 26",fg="green",bg="lightblue")
    y.pack(side=LEFT)
    btn_lahenda=Button(f1,text="Lahenda",font="Calibri 26",fg="green",command=Lahenda)
    btn_lahenda.pack(side=LEFT)
    btn_graafik=Button(f1,text="Graafik",font="Calibri 26",fg="green",command=Graafik)
    btn_graafik.pack(side=LEFT)


    aken.mainloop()


aken()



