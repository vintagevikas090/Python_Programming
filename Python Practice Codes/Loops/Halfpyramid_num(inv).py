
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''

r = int(input("Enter the no of rows: "))
for i in range(r,0,-1):
    for j in range(i,0,-1):
        print(j, end= " ")
    print()
