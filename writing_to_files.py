# Appending to the file

#test = open("file_name.txt", "a")
'''
a - you're adding some text at the end of the file.
In this case, the "write" method is used. 
If there is no file with the same name, a new one will be created.
The line will be added as many times as we run.
\n - to add information not to the end of the added line, but from a new line
'''

#test.write("\nThe meaning of these lines seems very interesting to me.")
#test.close()

# Writing to the file

second_test = open("new_file.txt", "w")
second_test.write("This will create a new file with this line")
second_test.close()

# There is also a writelines() method that takes a list of lines.