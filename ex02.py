''' Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
option end='' into the print function to fill the screen horizontally.]'''
while True:
    username = input("Enter your name: ")
    for i in range(10):
        print(f"{username}", end=" ")
    break