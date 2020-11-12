#While loop
number = 0
endPoint = int(input("Please enter the end point for your list: "))
print("Element    Number")
if endPoint > 9:
    while number < 9:
        print(number+1,"        ",number)
        number += 1
        #number = number +1
    while number < endPoint:
        print(number+1,"       ",number)
        number += 1
elif endPoint < 9 or endPoint == 9:
    while number < endPoint:
        print(number+1,"        ",number)
        number += 1
        #number = number +1
""" Expected Output
Please enter the end point for your list: 4
Element    Number
1          0
2          1
3          2
4          3
"""
