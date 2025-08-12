
'''Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.'''

s1 = "aedfjcsd"
s2 = "ognvndffkere9ifdo"
result = ""
length = 0

if len(s1)>len(s2):
    length = len(s1)
else:
    length = len(s2)
    
for i in range(length):
    if i<len(s1):
        result = result + s1[i]
    if i<len(s2):
        result = result + s2[-(i+1)]
print(result)