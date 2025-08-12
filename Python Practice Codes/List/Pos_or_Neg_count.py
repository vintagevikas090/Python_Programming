#Python program to print and count positive/negetive numbers in a list

l = [12, -7, 5, 64, -14, 12, 14, -95, 3]
#positive no
poscount = 0
negcount = 0
for i in l:
    if i>0:
        poscount+=1
        print(i)
print("Total positive numbers are: ", poscount)

#negetive no
for i in l:
    if i <0 :
        negcount+=1
        print(i)
print("Total negetive numbers are: ", negcount)



#method 2 for counting
c1, c2=0, 0   

for i in l:
    if i>0:
        c1+=1
    else:
        c2+=1
print("positive:",c1, ";", "negetive:",c2)
