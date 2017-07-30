#William... Febuary 8th 2016

#program will show
#1. how to creat a .txt file
#2. How to write to a .txt file
#3. how to read from a text file

#1 and 2
f = open("test.txt","a") #opens file with name of "test.txt" if does file does not excist this line creates it
f.write("New End")
f.close() 

#3
#this reads only first line
file = open('test.txt', 'r')

print file.readline();#number in () indicates number of charecters to read

#this seems to read all lines
file = open('test.txt', 'r')

print file.readlines()

#does it more clean
file = open('test.txt', 'r')

for line in file:
    print line,

"""please note: this program doesn't really do anything usefull. It
was made as a demonstration.  Parts of it are useful for other programs.
Also note that the file it creates or scans is always in the same directory as
the program itself
"""
