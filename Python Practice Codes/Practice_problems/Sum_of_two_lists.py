'''You need to find the sum of the 2 input arrays/list treating them as two integers and 
put the result in another array/list i.e. output array/list will also contain only single digit at every index.'''

arr1 = [1,2,3,4]
arr2 = [3,4,5,6]
carry, num = 0, 0
temp, result = [], []
m = 4
n = 4 #arr2
k = max(m, n)+1 
j = n-1
for i in range(m-1, -1, -1):
    while j>=0:
        num = arr1[i]+arr2[j]+carry
        temp.append(num%10)
        carry = num//10
        break
    j = j-1
for i in range(len(temp)-1, -1, -1):
    result.append(temp[i])
for i in result:
    print(i, end=" ")