'''
* * * * * 

* * * * 

* * * 

* * 

* 
'''

r = int(input("Enter the number of rows: "))
for i in range(r,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("\n")
  