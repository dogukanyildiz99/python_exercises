sum = 0
for variable in range(1,6):
    print("\nPlease enter your grade for class ", variable)
    num = int(input())
    sum = sum + num
    print("Sum of the grades you have entered till class", variable,"is ",sum)
avrg = sum/variable
print("\nYour average for ", variable,"classes is ", avrg)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Expected Output
#Please enter your grade for class  1 :
#65
#Sum of the grades you have entered till class 1 is  65
#Please enter your grade for class  2 :
#76
#Sum of the grades you have entered till class 2 is  141
#Please enter your grade for class  3 :
#67
#Sum of the grades you have entered till class 3 is  208
#Please enter your grade for class  4 :
#77
#Sum of the grades you have entered till class 4 is  285
#Please enter your grade for class  5 :
#60
#Sum of the grades you have entered till class 5 is  345
#Your average for  5 classes is  69.0
#apple
#cherry
