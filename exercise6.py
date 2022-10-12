'''. Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.'''
x = eval(input("enter a number: "))


squared = x * x

print (f"The square of {x} is {squared}")



#solution 2


x = eval(input("Enter a number:"))

square = x * x

print("The square of ", x, "is", square, sep=" " )