#Maximum frequency character in String

s = "GeeksforGeeks"
l = []
for i in s:
    l.append(s.count(i))

min_count = max(l) 
for i in s:
    if s.count(i)==min_count:
        print(i)
        break
