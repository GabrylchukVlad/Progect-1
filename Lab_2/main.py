Bogdan = [10, 3, 8, 2, 12, 5, 4]
Nikita = [9, 5, 7, 3, 11, 6, 4]
Makar = [8, 4, 6, 2, 10, 5, 3]
Denis = [7, 3, 5, 1, 9, 4, 2]
print("Щоденник")
a=input("Введіть логін: ")
b=input("Введіть пароль: ")
c=0
d=0
if a=="Bogdan" and b=="B1234":
    for i in Bogdan:
        if i < 4:
            c+=1
        else:
            d+=1
    print("Оцінки: ", Bogdan,"Не задовільно - ", c,"Задовільно - ",d)
if a=="Nikita" and b=="N1234":
    for i in Nikita:
        if i < 4:
            c+=1
        else:
            d+=1
    print("Оцінки: ", Nikita,"Не задовільно - ", c,"Задовільно - ",d)
if a=="Makar" and b=="M1234":
    for i in Makar:
        if i < 4:
            c+=1
        else:
            d+=1
    print("Оцінки: ", Makar,"Не задовільно - ", c,"Задовільно - ",d)
if a=="Denis" and b=="D1234":
    for i in Denis:
        if i < 4:
            c+=1
        else:
            d+=1
    print("Оцінки: ", Denis,"Не задовільно - ", c,"Задовільно - ",d)