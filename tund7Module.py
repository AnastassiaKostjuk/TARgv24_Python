from random import *
#ulesanne
# def summa3(arv1:int, arv2:int, arv3:int)->int:
#     """Tagastab kolme taisarvu summa

#     :param int arv1: Esimene number
#     :param int arv2: Teine number
#     :param int arv3: Kolmas number
#     :rtype: int

#     """
#     summa=arv1+arv2+arv3
#     return summa

#ulesanne1
# def arithmetic(a:float, b:float,t:str)->any:
#     if t in i["+","-","+","/"]:
#         if b==0 and t=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(a)+t+str(b))
#     else:
#         vastus("Tundmatu tehe!")
#     return vastus

# #ulesanne2
# def is_year_leap(aasta:int)->bool:
#     if aasta%4==0:
#         v=True
#     else:
#         v=False
#     return v

#ulesanne3
# def square(a:float)->any:
#     S=a**2
#     P=4*a
#     d=(2)**(1/2)*a
#     return S,P,d

#ulesanne4
# def season(month:int)->str:
#     if month in [1,2,12]:
#         season="talv"
#     elif month in [3,4,5]:
#         season="kevad"
#     elif month in [6,7,8]:
#         season="suvi"
#     elif month in [9,10,11]:
#         season="sugis"

#     return season

#ulesanne5
# def bank(a:float,years:int)->float:
#     for i in range(years):
#         a*= 0.1  # Увеличиваем вклад на 10%
#     return a

#ulesanne6
def is_prime(a=randint(0,1000))->bool:
    print(a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v=False
    return v

#ulesanne 8
# def XOR_cipher(text:str, voti:int)->str:
#     kodeeritud=""
#     for symbol in text:
#         kodeeritud+=chr(ord(symbol)^voti)
#     return kodeeritud