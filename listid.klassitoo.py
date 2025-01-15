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
nimed=[]
for i in range(5):
    nimi=input(i+1, ".Nimi: ")
    nimed.append(nimi)