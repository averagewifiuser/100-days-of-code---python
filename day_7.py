###Lesson 11: FIle Handling

f = open("readFile.txt")
#f=open("readFile.txt", "rt") r is for read, t is for text and they are default values

print(f.read()) # reading a file

#read first 5 characters of a fil
print(f.read(5))

#readon one line
print(f.readline())

#looping through the file, let's you read it line by line

#close file
f.close()

'''
Note: You should always close your files, 
in some cases, due to buffering, changes
made to a file may not show until you close the file.
'''

#will append the end of the file
f = open("readFile.txt", "a")
f.write("This write is from python")
f.close()

f = open("readFile.txt", "r")
print(f.read())
f.close()

#will rewrite the entire file
f = open("readFile.txt", "w")
f.write("I deleted the intial content")
f.close()

f = open("readFile.txt", "r")
print(f.read())
f.close()

#create file, returns error is the file exists
# f = open("newfile.txt", "x")
# f.close() 


# fw = open("newfile.txt", "a")
# fw.write("Made this new new file!")
# fw.close()


#"a" and "w" could be used, they would create
#file if it doesn't exist and write to them
#returns no error if they exist
fw = open("writeFile.txt", "w")
fw.write("New New write file!")
fw.close()


fd = open("deleteFile.txt", "x")
fd.close()

import os

os.remove("deleteFile.txt")

#remove folders
#os.rmdir("foldername")

#you can only remove empty folders.