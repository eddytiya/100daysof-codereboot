# read,readlines and other methods

f=open('myfile.txt','r')

while True:
    line=f.readline()
    if not line:
        break
    print(line)

'''printing student mks using readlines'''    

f = open('myfile2.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)


'''createa a new file with line 1 line 2 and line 3 in new lines'''
f = open('myfile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()