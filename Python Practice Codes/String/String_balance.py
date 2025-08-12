

'''Write a program to check if two strings are balanced. For example, 
strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter.'''

s1 = "ekdsf"
s2 = "dsficinaensdek"

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] in s2:
            j = j+1
            if j == len(s1):
                print("Balanced")
                break
            else:
                continue
        else:
            print("Not balanced")
            break
   