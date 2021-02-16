#coding:utf-8
import random
liste=range(50) #50 sayılı bir liste oluşturdum sayısal lotoyu bu listeden çekicez
print"Tahmin Ettiğiniz Sayılar"
liste1=[1,2,3,4,5,6] #Bu bizim tahmin ettiğimiz değerler.
print liste1
print "Rastgele Seçilen Sayılar"
list = random.sample(liste,6)#sample komutu oluşutrudğumuz listeden rastgele 6 tane değer seçiyor. Bu seçtiğimiz değerleri x adı altında birleştirdim.
print list
#count komutu sample'nin oluşturduğu listede bizim tahmin ettiğimiz sayıların olup olmadığını buluyor.
if 1 in list:
    print "Tebrikler",1,"Sayısını Bildiniz."
if 2 in list:
    print "Tebrikler",2,"Sayısını Bildiniz."
if 3 in list:
    print "Tebrikler",3,"Sayısını Bildiniz."
if 4 in list:
    print "Tebrikler",4,"Sayısını Bildiniz."
if 5 in list:
    print "Tebrikler",5,"Sayısını Bildiniz."
if 6 in list:
    print "Tebrikler",6,"Sayısını Bildiniz."






