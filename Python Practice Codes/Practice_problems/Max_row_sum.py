# Largest row sum in a 2D Lists
l = [[1,2,6], [3,4,4], [9,1,2, 4]]

# Method 1
sum= 0
for i in l:
    temp = 0
    for j in i:
        temp+=j
    if temp>sum:
        sum = temp
print(sum)

# Method 2
li = []
for i in l:
    sum = 0
    for j in i:
        sum+=j
    li.append(sum)
print(max(li))