from datetime import *
from calendar import *
from random import *
from math import *

#ülesanne 1
# päevadekogus = monthrange(2024,11)[1] #2024 - нулевая позиция и 11 - 1-ая позиция/calendar modulist
# print(monthrange(2024,11)[1])

# tana = date.today() #nimetus() - funktsioon
# tanaf = date.today().strftime("%B %d, %Y")
# print(f"Tere! Täna on {tanaf}")
# d = tana.day #nimetus - omadus
# m = tana.month
# y = tana.year
# print(d)
# print(m)
# print(y)

# detsP = monthrange(2024,12)[1] #31
# novP = monthrange(2024,11)[1] #30
# jaak = detsP + novP - d
# jaak2 = novP - d
# print(f"Aasta loppuni on {jaak}")
# print(f"Kuu loppuni on {jaak2}")

#ülesanne 2
# vastus1 = 3 + 8 / (4 - 2) * 4
# vastus2 = 3 + 8 / 4 - 2 * 4
# vastus3 = (3 + 8) / (4 - 2) * 4
# print(vastus1,"\n",vastus2,"\n",vastus3)

#ülesanne 3

#1 variant
# try:
#     r = float(input("Sisesta R: "))
#     Sk = pi*r**2 #площадь круга
#     Lk = 2*pi*r
#     Skv = (2*r)**2
#     Lkv = 2*r*4
#     print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala on {Skv}\nRuudu umbermoot on {Lkv}")
# except:
#     print("On vaja number!")

#2 variant
r = int(random()*100) #0.0...1.0
print(f"r = {r}")
Sk = pi*r**2 #площадь круга
Lk = 2*pi*r
Skv = (2*r)**2
Lkv = 2*r*4
print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala on {Skv}\nRuudu umbermoot on {Lkv}")

