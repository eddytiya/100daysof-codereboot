##dictmethods

emp1={
    122:45,
    123:89,
    567:69,
    670:69
}

emp2={
    222:67,
    566:90
}

#update
#suppose ep1 is senior boss and ep2 is sub boss
#so the boss anwts to create the data base for it self with all the employees
print(emp1)
emp1.update(emp2)
print(emp1)

#clesr()to empty any dict
##emp1.clear()
#print(emp1)

#creating an empty dict
empty={}
print(empty)

#pop
emp1.pop(122)
print(emp1)

emp1.popitem()#removes last tiem from list
print(emp1)

#del emp1[122]

