arr1 = [6,9,8,5]
arr2 = [0]
n, m = len(arr1), len(arr2)

num, digit, carry = 0,0,0
result_size = max(m, n) + 1
#print(result_size)
result = [0] * result_size
i,j = n-1, m-1 
k = len(result)-1

while i>=0 or j>=0:
    if i>=0:
        digit1 = arr1[i]
    else:
        digit1 = 0
        
    if j>=0:
        digit2 = arr2[j]
    else:
        digit2 = 0
           
    num = digit1 + digit2 + carry
    digit = num%10
    carry = num//10
    result[k]=digit
    
    i-=1
    j-=1
    k-=1
    
if m ==1 and n==1 and arr1[0] + arr2[0]<10:
    result.pop(0)   
if carry > 0 :
    result[0]=carry
    
for i in result:
    print(i, end=" ")