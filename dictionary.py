student = {"name":"miracle","age":13,"country":"Uk","city":"middlesbrough","gender":"male","Height":5.8}

print(len(student))
print(student["name"])
print(student)

print(student.keys())
print(student.values())

if "country" in student:
    print("it's present")
else:
    print("it's not")

student ["mood"]="happy" 
print(student)
student["talented"]="yes"
print(student)

del (student["age"])
print(student)

student ["city"]="lagos"
print(student)
student["Height"]=6
print(student)

student["marks"]=[99,98,32,56,86,100]
print(student)

print(student["marks"][0])
print(len(student["marks"]))

for item in student:
    print(item)
    