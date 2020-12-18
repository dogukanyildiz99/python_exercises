dosya = open("python.txt",encoding = "utf-8")
print(dosya.read())
dosya.close()

dosya = open("python.txt",encoding = "utf-8") #line line okuma
print("\n")
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
dosya.close()

dosya = open("python.txt",mode="a",encoding="utf-8") #append modu yazma ve olusturma icin kullanılır
dosya.write("\nGüzel bir egitimdi")
dosya.close()

dosya = open("python.txt",encoding = "utf-8")
print(dosya.read())
dosya.close()

""" Expected Output
Merhaba Dünya
Python programlama
Python çok zevkli


Merhaba Dünya

Python programlama

Python çok zevkli
Merhaba Dünya
Python programlama
Python çok zevkli
Güzel bir egitimdi
"""
