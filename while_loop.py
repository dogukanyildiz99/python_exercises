#While loop
number = 0
endPoint = int(input("Please enter the end point for your list: "))
print("Element    Number")
while number < 9:
    print(number+1,"        ",number)
    number += 1
    #number = number +1
while number < endPoint:
    print(number+1,"       ",number)
    number += 1
""" Expected Output
Please enter the end point for your list: 27
Element    Number
1          0
2          1
3          2
4          3
5          4
6          5
7          6
8          7
9          8
10         9
11         10
12         11
13         12
14         13
15         14
16         15
17         16
18         17
19         18
20         19
21         20
22         21
23         22
24         23
25         24
26         25
27         26
"""
