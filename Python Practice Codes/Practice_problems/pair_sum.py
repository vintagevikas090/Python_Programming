x = int(input())
l = [1, 3, 6, 2, 5, 4, 3, 2, 4]
pair = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i]+l[j]==x:
            pair+=1
print(pair)