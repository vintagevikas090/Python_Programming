#print URL present in a string

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
l = string.split()
print(l)
res = []
for i in l:
    if i.startswith("https:") or i.startswith("http:"):
        res.append(i)

print("Detected URLs in given string: ")
for i in res:
    print(i)
