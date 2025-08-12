'''For a given string(str), remove all the consecutive duplicate characters.
'''
str = input()
s = ""
for i in range(len(str)):
    temp = str[i]
    if i+1<len(str) and str[i] == str[i+1]:
        pass
    else:
        s = s+str[i]
    
print(s)