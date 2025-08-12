#remove elements from front and rear

s = input("Enter a string: ")
cut = int(input("Enter the number of character you wanna remove from start: "))
print(s[cut:])

rcut = int(input("Enter the number of character you wanna remove form end: "))
print(s[:(len(s)-rcut)])