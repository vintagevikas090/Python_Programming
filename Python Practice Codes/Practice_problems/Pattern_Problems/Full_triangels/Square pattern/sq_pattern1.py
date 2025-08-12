'''
for n == 4
* * * * 
* * * * 
* * * * 
* * * * 
'''

n = int(input("No of rows: "))
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print()