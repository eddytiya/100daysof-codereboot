#seek(),tell()
'''suppose u want to edit the 6th emement of a file u can use seek method to do so'''

with open('sample.txt', 'r') as f:
  f.seek(10)

  #read the data of next 5 bytes
  data=f.read(5)
  print(data)


#tell()
with open('sample.txt', 'r') as f:
  f.seek(10)

  #read the data of next 5 bytes
  print(f.tell())#The tell() function returns the current position within the file, in bytes. 
  data=f.read(5)
  print(data)
  

  #truncate ()

with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)#print only the first 5 letters in file

with open('sample.txt', 'r') as f:
  print(f.read())