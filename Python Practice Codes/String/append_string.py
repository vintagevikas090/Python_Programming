
#Append new string in the middle of a given string

s1 = "string"
s2 = "Vikas"
midpt = int(len(s1)/2)
nstr = s1[:midpt] + s2 + s1[midpt:]
print("Respective string is ", nstr)