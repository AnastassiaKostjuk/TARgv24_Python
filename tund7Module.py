#ulesanne1
# def summa3(arv1:int, arv2:int, arv3:int)->int:
#     """Tagastab kolme taisarvu summa

#     :param int arv1: Esimene number
#     :param int arv2: Teine number
#     :param int arv3: Kolmas number
#     :rtype: int

#     """
#     summa=arv1+arv2+arv3
#     return summa

#ulesanne2
# def arithmetic(a:float, b:float,t:str)->any:
#     if t in i["+","-","+","/"]:
#         if b==0 and t=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(a)+t+str(b))
#     else:
#         vastus("Tundmatu tehe!")
#     return vastus

#ulesanne3
def is_year_leap(aasta:int)->bool:
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
