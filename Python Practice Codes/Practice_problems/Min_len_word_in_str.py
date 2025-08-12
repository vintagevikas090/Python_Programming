# Minimum Length Word

s = input()
l = s.split()
min = len(s)
st = ""
for i in l:
    # temp = 0
    # for j in i:
    #     temp +=1
    temp = len(i)
    if temp<min:
        min = temp
        st = i
print(st)
