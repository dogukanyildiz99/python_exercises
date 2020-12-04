#DOGUKAN YILDIZ 20360859095
numA = int(input("Please enter an integer value for x:"))
numB = int(input("Please enter another integer value for range:"))
print("Results of the equation from numbers",numA,"to",numB,"are below.\n")
while numA <= numB:
    y= numA*numA + 3*numA - 4
    numA += 1
    print("y value for x =",numA-1,"is:",y)

""" Expected Output
Please enter an integer value for x:1
Please enter another integer value for range:6
Results of the equation from numbers 1 to 6 are below.

y value for x = 1 is: 0
y value for x = 2 is: 6
y value for x = 3 is: 14
y value for x = 4 is: 24
y value for x = 5 is: 36
y value for x = 6 is: 50 """
