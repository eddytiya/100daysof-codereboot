#tuple methods

#we need to convert tuple into list if we want to manipulate the tuple

countries=("India","australia","england","argentina","spain","germany","finland")

print(type(countries))
listy=list(countries)
print(type(listy))

#concat
countries2=("UAE","USA","UK")

united=countries + countries2
print(united)

tuple1=(9,1,2,3,2,3,1,3,2)
res=tuple1.count(3)
print(f"the number of occurrences is {res}")

lent=len(united)
print(lent)