#Cloning a list to another
l =  [12, 35, 9, 56, 24]
copy = []
#M1
for i in l:
    copy.append(i)
print(copy)
#M2
copy = l[::1]
print(copy)
#M3
copy.extend(l)
print(copy)
