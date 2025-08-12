'''
Print Minimum of the array using recursion
Hint: Keep on passing minimum value from top to down
'''
  
def print_min(lst, minVal = 100000):
    if len(lst) ==1:
        print(lst[0])
        return 
    if lst[0] < minVal:
        minVal = lst[0]
    print_min(lst[1:], minVal)

print_min([2,6,2,8,4])