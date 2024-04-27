import os
#print folders
folders=os.listdir("dataa")
print(os.getcwd())
'''prints current working directory'''
os.chdir("/Users")
print(os.getcwd())


# #printing all folders content
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"dataa/{folder}"))
          