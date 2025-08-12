
'''Python program to check if a string has at least one letter and one number'''

s="good 84after5noon Vikas"
count,c1,c2 = 0,0,0

for i in s:
    if i.isdigit():
        c1+=1
    if i.isalpha():
        c2+=1
count = c1+ c2
#print(c1,c2,len(s))
if count>0:
    print("True")
else: 
    print("False")
