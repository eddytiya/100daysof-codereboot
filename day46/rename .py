import os

#this program renames the 11folders 11 folders in dataa folder

for i in range(0,11):
    os.rename(f"dataa/Day{i+1}",f"dataa/tutorial{i+1}")
#changing the day name to tutorial using the OS module