#Dogukan YILDIZ 20360859095
d = 0
dNum = int(input("Please enter a number to calculate for multiplication table: "))
print("Multiplication table for",dNum,":")
while d <= 10:
    result = d*dNum #Multiplication
    d += 1 
    print(dNum,"x",d-1,"=",result)

"""
Please enter a number to calculate for multiplication table: 7
Multiplication table for 7 :
7 x 0 = 0
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
"""
