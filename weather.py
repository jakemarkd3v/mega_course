def weather_condition(temperature):
    if temperature > 7:
        print("Weather is warm")

    else:
        print("Weather is cold")


temp = eval (input("Enter the temperature:"))

weather_condition(temp)