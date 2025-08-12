
'''Python Program to Accept the Strings Which Contains all Vowels only'''

s = input("Enter a string containing all vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
res = []
for i in s:
    if i in vowels:
       res.append(i) 
    else:
        pass
if len(res)==5:
    print("Accepted")
else:
    print("Not Accepted")
