# Count the Number of matching characters in a pair of string

str1 = 'abcdef'
str2 = 'defghia'
c = 0
for i in str1:
    for j in str2:
        if i == j:
            c+=1
print(c)
