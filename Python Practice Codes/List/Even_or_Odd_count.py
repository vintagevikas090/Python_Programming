

#Python program to print and count even/odd numbers in a list

l =  [2, 7, 5, 64, 14, 70, 11, 20, 4, 100]

#printing even no
evencount = 0
oddcount = 0
for i in l:
    if i%2 == 0:
        evencount+=1
        print(i)
print("Total even numbers are: ", evencount)
        
#printing odd no
for i in l:
    if i%2 != 0:
        oddcount+=1
        print(i)
print("Total odd numbers are: ", oddcount)

