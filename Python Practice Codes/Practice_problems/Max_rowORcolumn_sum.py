'''
 Largest of sum of each columns's/ row's sum in a 2D Lists
 '''

l = [[1,2], [3,4], [2, 4]]

#for column

sum1, col = 0, 0
n = 3
m = 2
for j in range(m):
    temp = 0
    for i in l:
        temp += i[j]  #for iterating vertical
    if temp>sum1:
        sum1 = temp
        col = j


# For Rows

sum2, row= 0, 0
for i in range(n):
    temp = 0
    for j in range(m):
        temp+=l[i][j]
    if temp>sum:
        sum = temp
        row = i


#Final Answers
sum, num = 0, 0
string = ''
if sum1>sum2:
    sum = sum1
    string = "column"
    num = col
else:
    sum = sum2
    string = "row"
    num = row
    
print(string, "No", num, "Has the highest sum = ", sum)
