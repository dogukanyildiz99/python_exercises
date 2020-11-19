check = [1,2,3]
for _ in check:
    question = "Please enter a license plate:"
    licensePlate = int(input(question))
    if licensePlate == 16:
        print("License plate you have entered is for Bursa")
    elif licensePlate == 17:
        print("License plate you have entered is for Çanakkale")
    elif licensePlate == 34:
        print("License plate you have entered is for Istanbul")
    else:
        print("Unknown license plate")
 """
 Please enter a license plate:16
License plate you have entered is for Bursa
Please enter a license plate:34
License plate you have entered is for Istanbul
Please enter a license plate:17
License plate you have entered is for Çanakkale
"""
