print("hello")
print(len("hello"))
print(len("he   llo"))
print("--------------")
mystring = "hellokombucha"
print(mystring[0])
print(mystring[1])
print(mystring[0:3])
print(mystring[-1])
print(mystring[4:-1])
print(mystring[0:9:2])
print(mystring[::2])
print(mystring[::-1])
print("concatenating this string with " + mystring)
print("--------------")
print("using .upper(): " + mystring.upper())
dan = "USA"
print(dan)
print(dan.lower())
newdan = dan.lower()
print(newdan)
can = "Hello World"
print(can)
print(can.split())
print(can.split('o'))
print("--------------")
username = "Sammy"
color = 'blue'
print("The " + username + " favorite color is " + color)
print("the {} favorite is {}".format(username,color))
print("--------------")
print("PYTHON 3.6 AND ABOVE!!!")
print("f string literals!!")
print(f"The {username} chose {color}")