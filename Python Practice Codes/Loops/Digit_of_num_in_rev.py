#print digit of a number in reverse order

num = int(input("Enter a number: "))
while num>0:
    digit = num%10
    print(digit)
    num = num // 10
