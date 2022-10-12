'''create a program that ask for  users name and then greets the user in the format 'Hello username !' '''


'''solution 1'''
from email import message


def salutation(username):
    print("Hello", username + "!")
    return username

username = input("Enter your name: ")

salutation(username)


'''solution 2'''

user_input = input("Enter your name:")

message = f"Hello {user_input} !"

print (message)