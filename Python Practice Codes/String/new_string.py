
#Create a string made of the first, middle and last character

s = input("Enter a string: ")
result = s[0]
l = len(s)
mid = l//2
mid_ele = s[mid]
result = result + mid_ele
result = result + s[l-1]
print(result)