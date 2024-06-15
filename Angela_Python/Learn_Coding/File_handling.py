# File is nothing but name of memory location on disk that stores data permanenty
# File handling is a mechanism through which we can handle (Read, write , create, append etc)
# Syntax:- File_obj = open('file_path', 'mode') 
# open() is a function to work with files and it takes two - parameter
# File Mode:- r = read, w = write, a = append, rt = bothe read & write, b = binary mode
# File operater:- create, read , write, copy, delete, close etc
# Where the following mode is supported:

# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data

file = open("C:\\Users\\HOME PC\\Desktop\\Python_Raaj\\Angela_Python\\Learn_Coding\filehandling.txt","w")
file.write("Fileban gayi hai")


print("File created succesfully")

