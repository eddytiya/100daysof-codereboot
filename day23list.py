l=[46,11,66,1,2,4,6]

# print(l)
# #methods
# l.append(7)
# print(l)

# l.sort()
# print(l)

# print(l.index(1))
# print(l)

# print(l.count(1))
# print(l)

#copy fun
m=l.copy()
m[0]=0#change the value of index 0
print(m)

M=[900,1000,1100]
l.extend(M)
print(l)

#or concat 2 lists

k=l+M
print(l)