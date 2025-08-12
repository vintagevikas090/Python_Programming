

#fibbonacci terms printing

limit = int(input("Enter the total no of terms you require for fibbonacci: "))
a, b = 0, 1
for i in range(limit):
    print(a, end= " ")
    nxtno = a+b
    a = b
    b = nxtno
