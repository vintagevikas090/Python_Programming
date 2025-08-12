print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Normal Division')
print('5. Integer Division')
print('Choose the operation to be performed: ')
n = int(input())
print('Enter the numbers: ')
if n>0 and n<6:
    a = int(input())
    b = int(input())
    if n ==1:
        print(a+b)
    elif n ==2:
        print(a-b)
    elif n ==3:
        print(a*b)
    elif n ==4:
        print(a/b)
    elif n ==5:
        print(a//b)
else:
    print('Enter a valid Choice')