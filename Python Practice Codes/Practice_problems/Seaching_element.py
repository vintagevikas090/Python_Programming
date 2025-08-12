# Searching element
l = [1, 2, 3, 4, 5, 6, 7, 88, 97676,34, 32, 22, 43,56]
n = int(input())

#method 1
flag = False
for i in range(len(l)):
    if n == l[i]:
        print('index of given number is: ', i)
        flag = True
        break
if flag is False:
    print(-1)
    
#method 2 (using function)
def search_index(li, num):
    #li is the list and num is number that is gonna be searched
    for i in range(len(li)):
        if n == li[i]:
            return i
    return -1

print(search_index(l,n))