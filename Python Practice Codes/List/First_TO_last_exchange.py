#program to interchange first and last elements in a list
l =  [12, 35, 9, 56, 24]

#M1
temp = l[0]
l[0]=l[-1]
l[-1]=temp
print(l)

#M2
temp = l[0]
l[0]= l[len(l)-1]
l[len(l)-1]= temp
print(l)
