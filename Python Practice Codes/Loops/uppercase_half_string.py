''' Uppercase Half String (after half part)'''

s = "Good Afternoon Vikas"
print(len(s))
mid = len(s)//2
print(s[mid])
for i in range(len(s)):
    if i < mid:
        print(s[i], end="")
    else:
        print(s[i].upper(), end="")
