#print all duplicates from a given string in Python
str ="Not Accepted"
s = len(str)
for i in range(s):
    temp = str[i]
    for j in range(s):
        if i+1<s and temp == str[i+1]:
            print(temp)
            break
