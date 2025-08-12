#avoid spaces in string length
count = 0
s = "Good   Afternoon"
for i in range(len(s)):
    if s[i]!= " ":
        count+=1
print(count)
print(len(s))
