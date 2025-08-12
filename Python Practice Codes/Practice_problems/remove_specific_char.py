'''
For a given a string(str) and a character X,
write a function to remove all the occurrences of X from the given string.
'''

str = input()
char = input()
new_str = ""
for i in str:
    if i == char:
        pass
    else:
        new_str+=i
print(new_str)