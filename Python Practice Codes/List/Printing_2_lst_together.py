
#printing two list simultanously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    for j in range(len(list2)):
        if j == i:
            print(list1[i], list2[j], end="")
    print()

