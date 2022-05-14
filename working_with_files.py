'''
Use the "open" function to open a file:

open("file_name.txt", "mode")

File name:
    relative path of the file / absolut path of the file / just the files name if both files are in the same directories

Mode:
The mode that i want to open the file in
    first mode is called read - r
    second mode is called write - w
    third mode is called append - a (you can append information onto the end of the file)
    fourth mode is means read and write - r+

Generally we are going to want to store this o pen file inside of a variable

variable = open("file_name.txt", "r")

Whenever we open the file we always want to make sure that we close the file as well.
So we also have "close" function

variable.close()

'''

test = open("file_name.txt", "r")
print(test.readable())  # How can we check that the file is readable. "Readable" function returns a boolean value.
print(test.read())  # "Read" function returns all the information that is in the file
test.close()

# .readline()
test = open("file_name.txt", "r")
print(test.readline())
print(test.readline())
test.close()

# .readlines()
test = open("file_name.txt", "r")
print(test.readlines())
test.close()

# .readlines()  *We can also refer to a string by its index
test = open("file_name.txt", "r")
print(test.readlines()[2])
test.close()

# We can use "readline" function with a for loop
test = open("file_name.txt", "r")
for lines in test.readlines():
    print(lines)
test.close()



