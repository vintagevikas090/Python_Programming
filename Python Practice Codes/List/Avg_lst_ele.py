
#Find sum and average of List in Python

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
sum, avg = 0, 0
for i in lst:
    sum+=i

total_ele = len(lst)
print("Sum of list elements is: ", sum)
avg = sum / total_ele
print("Average of list elements is : ", avg)
