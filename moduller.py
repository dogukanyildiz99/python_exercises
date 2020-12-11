#modüller-1
from time import* # from time import clock
zaman1 = clock()
print("What's your name?")
isim = input()
sleep(1)
print("What's your surname?")
soyisim = input()
sleep(1)
print("Your full name is",isim,soyisim)

""" time modülünü iki sekilde ekleyebiliriz 
birincisi
import time
diğeri 
from time import*
buradaki '*' simgesinin amacı time modülündeki tüm fonksiyonları çağırmak
eğer sadece clock kullanacaksak
from time import clock
kullanmak daha verimli olacaktır"""
