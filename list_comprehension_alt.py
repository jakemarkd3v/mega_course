temps = [ 324, 323, 324, 657, -9999]

new_temps = [temp/10  if temp != -9999 else 0 for temp in temps]

print(new_temps)