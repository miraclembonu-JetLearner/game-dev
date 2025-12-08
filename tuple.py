tuple = ()

print(type(tuple))

num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print(num)

lang = ("python","java","html","visual","c++","anaconda")
print(lang[0])
print(len(lang))

for item in lang:
    print(item)

print("c"in lang)
print("python"in lang)

car = ("Bmw","Toyota","hydru","Mercides Benz")
color = ("red","blue","brown")

combined = car+color
print(combined)

number = (1,2)
repeat = number*5
print(repeat)

print(repeat.count(1))
print(car.index("Toyota"))

del color



print(num[3:8:1])
print(num[:12:])
print(num[::-1])
