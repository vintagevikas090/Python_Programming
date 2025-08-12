

'''Python program to capitalize the first and last character of each word in a string
'''
s="good afternoon Vikas"
l = len(s)
for i in range(l):
    if i==0 or i == l-1:
        print(s[i].upper())
    elif i+1<l and s[i+1]==" ":
        print(s[i].upper())
    elif i+2<l and s[i-1]==" ":
        print(s[i].upper())
    else:
        print(s[i])