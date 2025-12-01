houses = {"house1":"1234","house2":"1342","house3":"3455"}

house = str(input("enter your house number"))

if house in houses:
    password = str(input("enter your house password"))
    if houses [house] == password:
        print("welcome in")
    else:
        print("Invalid interaction")
else:
    print("unathuraised user")