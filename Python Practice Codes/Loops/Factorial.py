
#finding factorial


num = int(input("Enter the number"))
value = 1
for i in range(num, 0, -1):
    if num >0:
        value = value*num
        num = num-1
print(value)

