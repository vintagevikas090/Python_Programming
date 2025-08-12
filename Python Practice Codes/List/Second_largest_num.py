#Find second largest number in list

#M1
lst =[70, 11, 20, 4, 100]
#finding max num
temp1 = lst[0]
for i in lst:
    if i>temp1:
        temp1 = i
    else: 
        pass

#second largest number
temp2 = lst[0]
for i in lst:
    if i> temp2 and i<temp1:
        temp2 = i
    else: 
        pass
print(temp2)

#M2
lst.remove(max(lst))
print(max(lst))
