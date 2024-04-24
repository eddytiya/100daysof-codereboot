##dictionary
#key-value pair
#fast access to dictionary elements
#ordered collection of data items
#they store multile items in s single variable
#enclosed in curly brackets{}

# #example
# dict={
#     "aditya":"human being",
#     "spoon":"object"
# }

# print(dict)
# print(dict["aditya"])

# #example with intergers
# emp_id={
#     344:"aditya",
#     56:"anushka",
#     678:"sakshi",
#     567:"kohli"

# }
# print(emp_id)
# print(emp_id[567])

#myself
info={
    'name':"aditya",
    'age':21,
    'eligibility':True
}
# print(info)
# print(info['name'])
# print(info.get('eligibility'))
# '''
# info['name2"]=will thorew an error and disrupt your program so if u want to disrupt the flow of the program use the infomethod
# info.get('name2')=this will return the value as None and will not throw any error
# '''


# #accessing al the keys
# print(info.keys())
# #OR
# for key in info.keys():
#     print(info[key])

# #for values 
# print(info.values())
# for key in info.keys():
#  print(f"the value corresponding to the {key} is {info[key]}")

print(info.items())

for key,value in info.items():
    #print(key)
    #print(value)
    print(f"the value corresponding to the key {key} is {value}")