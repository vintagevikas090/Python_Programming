#prime no in a given range

limit = int(input("Enter the limit upto which you want the prime numbers: "))
for i in range(1,limit+1):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i)
