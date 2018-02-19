#coding:utf-8
"""
Bir online sistem için 100 adet kullanıcıya 8 karakterden oluşan şifre belirlenecektir.Oluşturulan şifreler bir listeye atılacaktır.
Şifre en az bir tane büyük harf,özel karakter,rakam,küçük harf içermelidir.

Oluşturulan şifrelerde yan yana 2 rakam olursa bulup hata mesajı verilmelidir...
"""
import random

sifreler=[]
bharf=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Z", "X"]
kharf=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "x"]
oharf=["!","%","?","*","#"]
rakam=["0","1","2","3","4","5","6","7","8","9"]
genel=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Z","X","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "x","!","%","?","*","#","0","1","2","3","4","5","6","7","8","9"]

for i in range(10):
    secim=[0,1,2,3]
    x=""

    for j in range(4):
        k=random.choice(secim)

        if k==0:
            x+=random.choice(bharf)
        elif k==1:
            x+=random.choice(kharf)
        elif k==2:
            x+=random.choice(oharf)
        else:
            x+=random.choice(rakam)
        secim.remove(k)

    for kalan in range(4):
        x+=random.choice(genel)

    sifreler.append(x)
print "Oluşturulan Şifreler Listesi===>",sifreler

for i in sifreler:
    for j in range(4):
        if i[j] in rakam and i[j+1] in rakam:
            print i,"Şifresi yan yana iki rakam bulunduğundan dolayı hatalıdır."