#day73:magic/dunder methods
'''
-starts with and ends with __
-used 
'''

class employee:
    name="aditya"
    def __len__(self):
        i=0    
        for c in self.name:
            i=i+1
        return i    


e=employee()
print(e.name)    
print(len(e))