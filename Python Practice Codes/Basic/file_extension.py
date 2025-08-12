''' Write a Python program that accepts a filename from the user and prints the extension of the file.'''

file_name = input("Enter the file name: ")
fextention = file_name.split(".")
#print(fextention)
print("File extention name is: ", fextention[-1])