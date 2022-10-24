temps = [221, 323, 434, 545]

new_temps =  []

for temp in temps:
    new_temps.append(temp/10)


print(new_temps)



#list comprehension approach 

temps = [221, 323, 434, 545]

new_temps = [temp/10 for temp in temps]

print(new_temps)
