# ##setmethods
# s1={1,2,5,6}
# s2={3,6,7}
# #union
# # print(s1.union(s2))
# print(s2.union(s1))
# # #update
# s1.update(s2)
# print(s1,s2)


cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
#union
cities3=cities.union(cities2)
print(cities3)
#intersection(same values)
print(cities.intersection(cities2))
'''cities.intersection_update(cities2)'''#this updates the cities set
print(cities)

#symmetric differece (values which r not common)
print(cities.symmetric_difference(cities2))

#disjoint means have same values or not
print(cities.isdisjoint(cities2))

print(cities.issuperset(cities2))

print(cities3.issubset(cities))

#adding 1 item to set
cities.add("mumbai")
print(cities)

#remove or discard
cities.remove("mumbai")
print(cities)