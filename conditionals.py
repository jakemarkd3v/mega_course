def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

monday_temps = [23.4,32.4,56.7]
std_grades ={"sam": 6.4, "john": 8.3, "love": 9.2}

print(mean(monday_temps))
print(mean(std_grades))
