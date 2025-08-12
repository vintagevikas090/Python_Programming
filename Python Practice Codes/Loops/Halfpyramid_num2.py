

'''
1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 
'''

r = int(input("Enter the no of rows: "))

for i in range(r+1):
    for j in range(1, i+1):
        print(j, end= " ")
        j = j+1
    print("\n")

