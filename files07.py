with open("files/veggies.txt", "a+") as myfiles:
    myfiles.write("\nOkra")
    myfiles.seek(0)
    content=myfiles.read()
print(content)