def sentence(phrase):
    interogatives = ("how", "what", "why")
    captalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(captalized)
    else:
        return "{}".format(captalized)
    

output = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break 
    else:
        output.append(sentence(user_input))

print(output)