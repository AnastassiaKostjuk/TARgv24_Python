from datetime import *
from calendar import *
from random import *
from math import *

#ülesanne 1
päevadekogus = monthrange(2024,11)[1] #2024 - нулевая позиция и 11 - 1-ая позиция/calendar modulist
print(monthrange(2024,11)[1])

tana = date.today() #nimetus() - funktsioon
tanaf = date.today().strftime("%B %d, %Y")
print(f"Tere! Täna on {tanaf}")
d = tana.day #nimetus - omadus
m = tana.month
y = tana.year
print(d)
print(m)
print(y)

detsP = monthrange(2024,12)[1] #31
novP = monthrange(2024,11)[1] #30
jaak = detsP + novP - d
jaak2 = novP - d
print(f"Aasta loppuni on {jaak}")
print(f"Kuu loppuni on {jaak2}")

#ülesanne 2
vastus1 = 3 + 8 / (4 - 2) * 4
vastus2 = 3 + 8 / 4 - 2 * 4
vastus3 = (3 + 8) / (4 - 2) * 4
print(vastus1,"\n",vastus2,"\n",vastus3)

#ülesanne 3

#1 variant
try:
    r = float(input("Sisesta R: "))
    Sk = pi*r**2 #площадь круга
    Lk = 2*pi*r
    Skv = (2*r)**2
    Lkv = 2*r*4
    print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala on {Skv}\nRuudu umbermoot on {Lkv}")
except:
    print("On vaja number!")

#2 variant
r = int(random()*100) #0.0...1.0
print(f"r = {r}")
Sk = pi*r**2 #площадь круга
Lk = 2*pi*r
Skv = (2*r)**2
Lkv = 2*r*4
print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala on {Skv}\nRuudu umbermoot on {Lkv}")

#ülesanne 4
D = 2.575 #mundi d
maa = 6378 #maa radius km
maa *= 100000 #maa raduis cm + maa=maa*100000
Lmaa = 2*pi*maa
kogus = int(Lmaa/D)
print(f"On vaja {kogus} mundi.\nMeil on vaja {kogus*2} eur")

#ülesanne 5
a = "kill-koll ".capitalize()
b = "killadi-koll ".capitalize()
print(a*2, b, a*2, b, a*4)

#ülesanne 6
a = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?""".upper()

b = """Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper()

print(a)
print()
print(b)

#ülesanne 7
d = float(input("длина прямоугольника: "))
s = float(input("ширина прямоугольника: "))
pr = 2*(d + s)
pl = d * s
print(f"периметр прямоугольника: {pr}")
print(f"площадь прямоугольника: {pl}")

#ülesanne 8
t = float(input("количество литров топлива в баке: "))
k = float(input("пройденные километры: "))
sr = t/k * 100
print(round(sr, 2))

#ülesanne 9
print("Средняя скорость составляет 29.9 км/ч.")
m = int(input("Время в минутах: "))
rasstojanie = 29.9 * (m / 60)
print(f"За {m} минут(ы) роллер преодолеет {round(rasstojanie, 2)} км.")

#ülesanne 10
m = int(input("время в минутах: "))
hours = m//60
rm = m % 60
print(f"{hours}:{rm:02d}")