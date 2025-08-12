

#Count occurrences of an element in a list
l =  [12,12, 35, 9, 56, 24]
#count of 12

print(l.count(12))
#M2
count= 0
for i in range(len(l)):
    if i+1<len(l) and l[i+1] ==temp :
        count+=1
print(count)
