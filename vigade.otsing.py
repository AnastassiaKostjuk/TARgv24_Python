# import * from math 
# print("Ruudu karakteristikud")
# a=input('Sisesta ruudu külje pikkus => ')
# S=a**2
# print("Ruudu pindala", S)
# P=4*a
# print("Ruudu ümbermõõt'', P)
# di=a*math.sqr(2)
# print("Ruudu diagonaal", round(di,2))
# print()
# print("Ristküliku karakteristikud"))
# b=input("Sisesta ristküliku 1. külje pikkus => ")
# c=input("Sisesta ristküliku 2. külje pikkus => ")
# S=b*c
# print(Ristküliku pindala', S)
# P=2(b+c)
# print("Ristküliku ümbermõõt", P)
# di=math.sqrt(b*2+c*2)
# print("Ristküliku diagonaal", round(di)
# print()
# print("Ringi karakteristikud")
# r=input(''Sisesta ringi raadiusi pikkus => ''))
# d=2r
# print("Ringi läbimõõt" d)
# S=pi()*r*2
# print("Ringi pindala", round(S))
# C=2pi()*r
# print("Ringjoone pikkus", round(C)

#правильный порядок
from math import *
print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => '))
S = a**2
print("Ruudu pindala:", S)
P = 4*a
print("Ruudu ümbermõõt:", P)
di = a*math.sqrt(2)
print("Ruudu diagonaal:", round(di, 2))
print()
print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b*c
print("Ristküliku pindala:", S)
P = 2 * (b+c)
print("Ristküliku ümbermõõt:", P)
di = math.sqrt(b**2+c**2)
print("Ristküliku diagonaal:", round(di, 2))
print()
print("Ringi karakteristikud")
r = float(input('Sisesta ringi raadiusi pikkus => '))
d = 2 * r
print("Ringi läbimõõt:", d)
S = math.pi*r**2
print("Ringi pindala:", round(S, 2))
C = 2 * math.pi * r
print("Ringjoone pikkus:", round(C, 2))