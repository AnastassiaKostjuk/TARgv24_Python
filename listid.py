import string

#ulesanne1
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="qwrtyplkjhgfdszxcvbnm"
# markid=string.punctuation # %&'()*+,-./:;<=>?@[]\^_`{|}~

# while True:
#     v=k=m=t=0
#     tekst=input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list=list(tekst)
#         print(tekst_list)
#         for taht in tekst_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsonanti:
#                 k+=1
#             elif taht in markid:
#                 m+=1
#             elif taht ==" ":
#                 t+=1
#     print("Vokaali: ", v)
#     print("Konsonanti: ", k)
#     print("Markid: ", m)
#     print("Tuhikud: ", t)



#ulesanne2
# nimed=[]
# for i in range(5):
#     nimi=input(f"{i+1}.Nimi: ")
#     nimed.append(nimi)
# print("Enne sorteerimist: ")
# print(nimed)
# nimed.sort()
# print("Sorteerimise parast: ")
# print(nimed)
# print(f"Viimasena lisatud nimi on: {nimi}") #{nimed[4]}, {nimed[-1]}
# v=input("Kas muudame nimeid?: ").lower()
# if v=="jah":
#     v=input("Nimi voi positsioon: N/P").upper()
#     if v=="P":
#         print("Sisesta nime asukoht")
#         v=int(input())
#         uus_nimi=input("Uus nimi: ")
#         nimed[v-1]=uus_nimi
#     else:
#         print("Sisesta nimi")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
#     print(nimed)
# #dublikatid 1
# dublta=list(set(nimed))
# print(dublta)
# #dublikatid 2
# dublta=[]
# for nimi in nimed:
#     if nimi not in dublta:
#         dublta.append(nimi)
# print("Mitte korduv loetelu 2.variant")
# print(dublta)

# vanused=[] #pustoj spisok
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sisestatud vanused: {vanused}")
# print(max(vanused))
# print(min(vanused))
# print(sum(vanused)/len(vanused))

#ulesanne 3
# Vartused=[]
# read=int(input("Reade kogus: "))
# for i in range(read):
#     arv=int(input("Arv: "))
#     Vartused.append(arv)
# print(Vartused)
# s=input("Sumbol: ")
# for vartus in Vartused:
#     print(vartus*s)

# print()

#ulesanne 4

indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

while 1:
    try:
        postiindex=int(input("Postiindeks: "))
        if len(str(postiindex))==5:
            break
        else:
            print("On vaja 5 sumboleid!")
    except:
        print("!!!")
print("Postiindeksi analuus: ")
index_list=list(str(postiindex))
s1=int(index_list[0])
print(f"Postiindeks {postiindex} on {indexid_list[s1-1]} piirkond")

