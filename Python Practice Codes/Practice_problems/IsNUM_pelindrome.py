n = int(input())
temp = n
rev = 0
digit = 0
while temp>0:
    digit = temp%10
    temp = temp //10
    rev = rev*10 + digit
    
print(rev == n)