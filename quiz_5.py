from math import*
x = int(input("Please enter a value for x coordinates:"))
y = int(input("Please enter a value for y coordinates:"))
z = sqrt(pow(x,2)+pow(y,2))
if z > 5:
    print("The coordinates you have entered is outside of the circle")
elif z < 5:
    print("The coordinates you have entered is inside of the circle")
elif z == 5:
    print("The coordinates you have entered is on the circle")
#Dogukan YILDIZ 20360859095