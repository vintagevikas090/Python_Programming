#Reversing a list

l =  [12, 35, 9, 56, 24]

#M1
print(l[::-1])

#M2
rev = []
for i in range(len(l)):
    rev.append(l[-1-i])
print(rev)

#M3
revs = []
for i in range(len(l)-1,-1, -1):
    revs.append(l[i])
print(revs)
