def SumofDigit(num):
    if num==0:
        return 0
    digit = num%10
    return digit + SumofDigit(num//10)

k = int(input())
print(SumofDigit(k))