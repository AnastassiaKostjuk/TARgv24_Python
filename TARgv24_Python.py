from random import * #*-kõik funktsioonid, randint as rd funktsioonide ümbernimetus

from math import * #pi kasutamiseks

#ülesanne 1
print("Tere tulemast!")
nimi = input("Mis on sinu nimi?").capitalize() #lower()-aaa, upper()-AAA, capitalize()-Aaa
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
try:
    vanus = int(input("Kui vana sa oled? "))
    print("Tere tulemast! Tervitan sind  "+ nimi + " Sa oled ", vanus, "aastat vana")
    print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")
except:
    print("On vaja numbreid sisestada!")


#ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

#ülesanne 3
kokku = randint(1, 1000)
print(f"Kokku on {kokku} kommi")
kommi = int(input("Mitu kommi sa tahad? "))
kokku = kokku - kommi
print(f"Jääk on {kokku} kommi")

#ülesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l = float(input("Ümbermõõt: "))
d = l/pi
print(f"Lääbimõõdu suurus on {round(d,2)}")
print('test')

#ülesanne 5
import math
N = float(input("Введите длину прямоуголника: "))
M = float(input("Введите ширину прямоуголника: "))
d = math.sqrt(N**2 + M**2)
print(d)

#ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# #ülesanne 7
print(input("Введите 5 целых чисел"))
arv1 = int(input())
arv2 = int(input())
arv3 = int(input())
arv4 = int(input())
arv5 = int(input())
summa = arv1 + arv2 + arv3 + arv4 + arv5
print("Summa on", summa)
keskmine = summa/5
print("Keskime on", keskmine)

#ülesanne 8
frog = """
   @..@
  (----)
 ( \__/ )
 ^^ "" ^^
"""
print(frog)

#ülesanne 9
a = int(input("Первая сторона равна: "))
b = int(input("Вторая сторона равна: "))
c = int(input("Третья сторона равна: "))
p = a + b + c
print("Периметр равен:", p)

#ülesanne 10
pitsa = 12.90
print("Pitsa on ",pitsa)
jootraha = 0.10 * pitsa
print("Jootraha on ",jootraha)
summa_kokku = pitsa + jootraha
print("Summa kokku on",round(summa_kokku,2))
summa = summa_kokku/2
print("kui palju peab igaüks maksma: ",round(summa,2))



