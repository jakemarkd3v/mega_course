'''Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes'''
x = eval(input("Enter a number:"))

print(x, (2*x), (3*x), (4*x),(5*x), sep="---")