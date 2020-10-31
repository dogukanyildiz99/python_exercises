print("Please start your answers with capital letter.")
question = "What's the weather like?"
print(question)
answer = input()
if answer =="Rainy":
    print("Do not forget to get your umbrella!")

question ="What's your name?"
print(question)
answer = input()
if answer =="Dogukan":
    print("We have the same name!")
else:
    print("We dont have the same name,",answer)

print("What season are we in?")
season = input()
if season == "Winter":
    print("It is the first season of the year.")
    print("Mind your step and keep yourself warm!")
elif season == "Spring":
    print("It is the second season of the year.")
    print("Enjoy the sun with blooming flowers!")
elif season == "Summer":
    print("It is the third season of the year.")
    print("Eat icecream, drink cold beverages and enjoy the sea!")
elif season == "Fall":
    print("It is the last season of the year.")
    print("Gingerbreads, pumpkins and beauty of the falling leaves.")
elif season == "Autumn":
    print("It is the last season of the year.")
    print("Gingerbreads, pumpkins and beauty of the falling leaves.")
else:
    print("We said the seasons!")

#Expected Output
#Please start your answers with capital letter.
#What's the weather like?
#Rainy
#Do not forget to get your umbrella!
#What's your name?
#Brian
#We dont have the same name, Brian
#What season are we in?
#Fall
#It is the last season of the year.
#Gingerbreads, pumpkins and beauty of the falling leaves.
