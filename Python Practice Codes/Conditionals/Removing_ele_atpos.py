'''program for removing i-th character from a string'''
s = "Hi there, I am Shahid"
#removing 7th element
n = 6
for i in range(len(s)):
    if i == n:
        print("",end="")
    else:
        print(s[i], end="")
