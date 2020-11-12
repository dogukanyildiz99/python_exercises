studentId = ["Dogukan","YILDIZ",21]

print("Our information: ",studentId)
print("Data type of the information is:",type(studentId))
print("Name of the student:",studentId[0])
print("Surname of the student:",studentId[1])
print("Age of the student",studentId[0]," is",studentId[2])

studentId.append("Undergraduate")

print("Updated information:",studentId)
print("Student status of ",studentId[0],studentId[1]," is",studentId[3])

""" Expected Output
Our information:  ['Dogukan', 'YILDIZ', 21]
Data type of the information is: <class 'list'>
Name of the student: Dogukan
Surname of the student: YILDIZ
Age of the student Dogukan  is 21
Updated information: ['Dogukan', 'YILDIZ', 21, 'Undergraduate']
Student status of  Dogukan YILDIZ  is Undergraduate """
