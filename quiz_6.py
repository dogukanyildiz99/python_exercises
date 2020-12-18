#Dogukan YILDIZ 20360859095
def  ucgenmi(a,b,c):
    if a < (b + c) and a > abs(b-c): #abs absolute fonksiyonudur mutlak degeri temsil eder
        print("Values you have entered does represent a triangle.")
    elif abs(c-a) < b < (c + a):
        print("Values you have entered does represent a triangle.")
    elif abs(a-b) < c < (a + b):
        print("Values you have entered does represent a triangle.")
    else:
        print("Values you have entered does NOT represent a triangle.")
    return (a,b,c)

a = int(input("Please enter an integer value for a:"))
b = int(input("Please enter an integer value for b:"))
c = int(input("Please enter an integer value for c:"))

ucgenmi(a,b,c)

"""Expected Output
Please enter an integer value for a:3
Please enter an integer value for b:4
Please enter an integer value for c:5
Values you have entered does represent a triangle.
"""
