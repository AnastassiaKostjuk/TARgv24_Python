
print("*** ARVUDE MÄNG ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Siseta täisarv => ")))
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga on mõttetu töö")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
        if b % 2 == 0:   #остаток от деления на ноль
            paaris += 1  #если =+, то это приравнивание
        else:
            paaritu += 1
        b = b // 10 #оставляет целую часть
    
    print("Paaris arv:", paaris)
    print("Paaritu arv:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Ümberpööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreem")
    print()
    # if c % 2 == 0:
    #     print(c, " - paaris arv. jagame 2.")
    # else:
    #     print(c, " - paaritu arv. korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
        if c % 2 == 0:
            print('{:>4}'.format(round(c))," - paaris arv, jagame 2.")
            c = c / 2
    else:
        print('{:>4}'.format(round(c))," - paaritu arv. korrutame 3, liidame 1 ja jagame 2.")
        c = (3*c + 1) / 2

    print('{:>4}'.format(round(c))," - Teoreem on toestatud")
    print()