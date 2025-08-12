'''Write a Python program that accepts the user's first and last name and
prints them in reverse order with a space between them.'''

fname = input("Enter your first name: ")
lname = input("Enter last name: ")

#method 1
fullname = fname+" "+lname
revname = fullname[::-1]
print(revname)

#method 2
rev_name = lname[::-1] +" "+fname[::-1]
print(rev_name)