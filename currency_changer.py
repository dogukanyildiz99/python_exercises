# Currency changer
USD_to_GBP = 0.66 # Bugünün döviz kuru
GBP_sign ='\u00A3'
dollars = int(input("Please enter $ to change: "))

# calculations
pounds = dollars * USD_to_GBP

print('Today, $' + str(dollars))
print('converts to ' + GBP_sign + str(pounds))

"""
Please enter $ to change: 3000
Today, $3000
converts to £1980.0 """
