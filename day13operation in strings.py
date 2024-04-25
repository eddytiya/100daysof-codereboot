#operation in strings
#strings are immitable
a="Aditya"
b="adityaa!!!!! !!!!!"
print(len(a))

print(a.upper())
print(a.lower())

print(b.rstrip("!"))#revover trailing symbols or whatever is stated

print(a.replace("Aditya","john"))#replaces all occurrences of aditya with john
#split():The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(b.split(" "))

blog="introduction to js"
print(blog.capitalize())#to capital the first letter of a line

#The center() method aligns the string to the center as per the parameters given by the user.
str1="welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))

#strip removes white spaces before and after the string
str2 = " Silver Spoon "
print(str2.strip())

str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

#count():counts the number of occurrences of the value stated
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

#endwith():checks if the string ends with the given value
tr1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

#We can even also check for a value in-between the string by providing start and end index positions.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

#find():checks for the first occurrences of the given value
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

#index():searches for the first occurrences of the given value and returns the index where it is present
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

#isrealnum():checksif the entire sting consists of a-z,A-Z,0-9
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

#The isalnum() method returns True only if the entire string only consists of A-Z, a-z.
str1 = "Welcome"
print(str1.isalpha())

#islower()
str1 = "hello world"
print(str1.islower())

#isprintable()
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())