#create a tip calculator
'''A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.'''


meal_price =  eval(input("Please, what is the  price of your meal?  "))

tip = eval(input("Hope you enjoyed your meal, how much would you be giving as a tip? "))

bill = meal_price + tip

print("Your bill is:","$", bill, sep="" )