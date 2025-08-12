

'''Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that
the new list should contain odd numbers from the first list and even numbers from the second list.'''

l = [1, 2, 3, 4, 6,9]
l1 = [234, 23, 232, 354, 45, 765, 54]
l2 = []
for i in l:
    if i % 2 != 0:
        l2.append(i)
for i in l1:
    if i % 2 == 0:
        l2.append(i)
        
print(l2)
