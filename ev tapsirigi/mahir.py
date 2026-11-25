# eded=float(input("Bir ədəd daxil edin:"))
# if eded>0:
#     print("Ədəd müsbətdir")
# elif eded<0:
#     print("Ədəd mənfidir")
# else:
#     print("Eded sifirdir")



# eded=int(input("Tam ədəd daxil edin:"))

# if eded %2==0:
#     print("Cüt ədəddir")
# else:
#     print("Tək ədəddir")



# bal=float(input("Balı daxil edin:"))

# if bal>=51:
#     print("Keçdi")
# else:
#     print("Kəsildi")



# yas=int(input("Yaşınızı daxil edin:"))

# if 0<= yas <=12:
#     print("uşaq")
# elif 13<= yas <=17:
#     print("yeniyetmə")
# elif yas>=18:
#     print("yetkin")
# else:
#     print("Yanlış yaş daxil edilib")



# a=float(input("Birinci ədədi daxil edin"))
# b=float(input("İkinci ədədi daxil edin"))

# if a>b:
#     print(f"ən böyük ədəd:{a}")
# elif b>a:
#     print(f"ən böyük ədəd:{b}")
# else:
#     print("ədədlər bərabərdir.")



# soz=input("Bir söz daxil edin:")
# print(soz.upper())


# soz=input("Bir söz daxil edin:")
# print("Simvolların sayı:",len(soz))



# bal=float(input("0-100 arası bal daxil edin:"))

# if 90<= bal <=100:
#     print("əla")
# elif 70<= bal <=89:
#     print("yaxşı")
# elif 50<= bal <=69:
#     print("kafi")
# elif 0<= bal <=49:
#     print("qeyri-kafi")
# else:
#     print("yanlış bal")



# a=float(input("Birinci ədədi daxil edin:"))
# op=input("Operator daxil edin (+,-,*,/):")
# b=float(input("İkinci ədədi daxil edin: "))

# if op=="+":
#     print("nəticə:",a+b)
# elif op=="-":
#     print("nəticə:",a-b)
# elif op=="*":
#     print("nəticə:",a*b)
# elif op=="/":
#     if b==0:
#         print("Xəta:  sıfıra bölmək olmaz!!!")
#     else:
#         print("nəticə:",a/b)
# else:
#     print("Yanlış operator daxil edilib")



# soz=input("Bir söz daxil edin:")

# if len(soz)==0:
#     print("Söz boşdur!!!")
# else:
#     print("ilk hərf:",soz[0])
#     print("son hərf:",soz[-1])



# soz=input("Bir söz daxil edin:").lower()
# saitler="aıouöeəi"
# say=0

# for herf in soz:
#     if herf in saitler:
#         say+=1

# print("sait hərflərin sayı:",say)




# numbers=[13,7,8,22,10,6,24]
# cut_ededler=[]

# for eded in numbers:
#     if eded %2==0:
#         cut_ededler.append(eded)

# print("cüt ədədlər:",cut_ededler)



# soz=input("Bir söz daxil edin:")
# say=0

# for herf in soz:
#     if herf=="a" or herf=="A":
#         say+=1

# print("'a'hərfinin sayı:",say)



# username=input("İstifadəçi adını daxil edin:").strip()

# if len(username)<5:
#     print("username qısadır")
# else:
#     print("username qəbul edildi")



# secret=7
# while True:
#     texmin=int(input("Ədədi tapın:"))

#     if texmin>secret:
#         print("Daxil etdiyiniz ədəd böyükdür")
#     elif texmin<secret:
#         print("Daxil etdiyiniz ədəd kiçikdir")
#     else:
#         print("Təbriklər!!! Düzgün ədədi tapdınız")
#         break



# soz=input("Bir söz daxil edin:")
# say=soz.lower().count("a")
# print(f"Sözdə 'a' hərfi  {say}  dəfə təkrarlanır.")




cumle=input("Bir cümlə daxil edin:")
yeni_cumle=cumle.replace(" ","-")
print(yeni_cumle)