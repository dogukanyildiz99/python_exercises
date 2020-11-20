cityNames = ["Adana","Istanbul","Izmir","Bursa","Ankara"]
for city in cityNames:
    if city == "Istanbul":
        print(city)
        print(city[0:2],city[7:5:-1])
    elif city == "Ankara":
        print(city)
        print(city[0:2],city[5:3:-1])
    else:
        print(city)
        print(city[0:2],city[4:2:-1])
"""
Adana
Ad an
Istanbul
Is lu
Izmir
Iz ri
Bursa
Bu as
Ankara
An ar
"""
