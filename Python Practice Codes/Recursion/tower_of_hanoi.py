def tower_hanoi(n,a,b,c):
    if n==1:
        print("move 1st disk from", a, "to", c)
        return
    tower_hanoi(n-1,a,c,b)
    print("move",n,"th disk from",a,"to",c)
    tower_hanoi(n-1,b,a,c)

tower_hanoi(2,"s","h","d")


'''
say in 1st part...
n-1 disks are moved to b and 
biggest from a to c

now since c has the biggest disk, putting any other on it won't disturb the balance..
So the disks from b can be moved to c using a

'''