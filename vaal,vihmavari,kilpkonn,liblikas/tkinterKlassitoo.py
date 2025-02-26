from tkinter import *
from matplotlibb import *
global varv,tekst
def varvi_valik():
    varv="white"
    if tekst.get()!="":
        tekst.configure(bg="lightblue")
        varv=tekst.get()
    else:
        tekst.configure(bg="red")
    return varv

def figuur(varv:str):
    #global varv
    #varv=varvi_valik()
    valik=var.get()
    if valik==1:
        Vaal(varv)
    elif valik==2:
        Vihmavari(varv)
    else:
        Prillid()
        print("Joonestan hiljem")

aken=Tk()
aken.geometry("400x800")
aken.title("Graafikud")
pealkiri=Label(aken,text="Erinevad piltid Matplotlip abil",font="Calibri 24",fg="green",bg="lightpink",pady=20,width=200)

var=IntVar()
r1=Radiobutton(aken,text="Vaal", font="Calibri 18", variable=var, value=1, command=lambda:figuur(varv=varvi_valik()))
r2=Radiobutton(aken,text="Vihmavari", font="Calibri 18", variable=var, value=2, command=lambda:figuur(varv=varvi_valik()))
r3=Radiobutton(aken,text="Prillid",font="Calibri 18",variable=var,value=3,command=lambda:figuur(varv=varvi_valik()))
tekst=Entry(aken,font="Calibri 24",fg="green",bg="lightpink",width=200)
nupp=Button(aken,text="Varvi valik",font="Calibri 24",fg="green",bg="lightpink",command=varvi_valik)

pealkiri.pack() #place(x=...,y=...),grid(column=...,row=...)
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
aken.mainloop()


