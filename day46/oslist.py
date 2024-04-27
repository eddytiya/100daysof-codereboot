import os
#print folders
folders=os.listdir("dataa")
print(folders)
#printing all folders content
for folder in folders:
    print(folder)
    print(os.listdir(f"dataa/{folder}"))
          