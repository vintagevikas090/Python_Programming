#Odd Frequency Characters

s = "GeeksforGeeks"
l = []
for i in s:
    if (s.count(i)) % 2 !=0:
        print(i)

