users = {"user1":"ww1","user2":"password2","user3":"password3","user4":"password4","user5":"password5",
         "user6":"password6","user7":"password7","user8":"password8","user9":"password9","user10":"password10"}

username = input("enter your username")

if username in users:
    password =input("enter your password")
    if users [username] == password:
        print("you are now logged in")
    else:
        print("Invalid password")
else:
    print("you are not a valid user")