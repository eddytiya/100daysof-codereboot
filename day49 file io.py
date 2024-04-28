#file handling I/O

#read mode:opens a file only to read
f=open("myfile.txt",'r')
#to see file content
text=f.read()
print(text)
f.close()
#'r mode is default if u dont state file will itself open in read mode

#WRITING TO A FILE
'''writing to a file will overrite its content if u want to add content then you will have to use append mode'''
f=open('myfile.txt','w')
f.write('hello world')
f.close()


#APPEND
f=open('myfile.txt','a')
f.write('hello world appended\n')
f.close()

'''
There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).

'''