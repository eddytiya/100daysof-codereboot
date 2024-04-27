import os
if(not os.path.exists("dataa")):
    os.mkdir("dataa")#creates a new folder called data

#this program creates 11 folders in dataa folder

for i in range(0,11):
    os.mkdir(f"dataa/Day{i+1}")


#renaming