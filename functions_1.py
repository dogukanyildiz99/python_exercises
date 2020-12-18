#Fonksiyonlar 1

def Square(a):
    print("Square of your number is: ",a**2)

a = int(input("Please enter a number: "))
Square(a)

def Kare(a):
    sonuc = a**2
    return sonuc # bu degeri daha sonra da kullanmak istersek
print("Square of the number is:",Kare(a))

def FullName(name,surname):
    return name + " " + surname

isim = input("Please enter your name: ")
soyisim = input("Please enter your surname: ")
print("Your full name is ",FullName(isim,soyisim))

""" Expected Output
Please enter a number: 5
Square of your number is:  25
Square of the number is: 25
Please enter your name: Dogukan
Please enter your surname: YILDIZ
Your full name is  Dogukan YILDIZ
"""