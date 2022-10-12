'''write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
'''
x = eval(input("Give a number:"))
y = eval(input("Give a number:"))
z = eval(input("Give a number:"))

numbers = [x,  y, z]
total =  x  + y + z 

average = total / len(numbers)


print("The total of the numbers you inserted is", total)

print("The average of the numbers you inserted is", average)