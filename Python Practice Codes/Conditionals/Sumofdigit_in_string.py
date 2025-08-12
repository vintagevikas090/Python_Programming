
'''Calculate the sum and average of the digits present in a string'''

str1 = "PYnative29@#8496"
sum = 0
count = 0
for i in str1:
    if (i.isdigit()):
        sum = sum+int(i)
        count = count+1
print("Sum of the digits is: ", sum)
avg = sum / count
print("Average of the digits present in string is: ", avg)
