#iteration over dictionaries
std_grades ={"sam" : 45, "joy" : 60, "ken" :  57}

for grades in std_grades.items():
    print(grades)
    print("***")

for grades in std_grades.values():
    print(grades)
    print("***")

for grades in std_grades.keys():
    print(grades)
    print("***")
    
