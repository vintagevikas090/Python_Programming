
'''Write a Python program to count the number of even and odd numbers in a series of numbers'''

l = range(100)
print(l)
for i in l:
    if i%2 == 0:
        print("even  ", i)
    else:
        print("odd  ", i)

