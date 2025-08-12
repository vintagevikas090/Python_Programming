# Check if a given string is binary string or not
str1 = "01010101010"
l = len(str1)

for i in range(l):
    if str1[i] == "0" or str1[i] == "1":
        if i == l-1:
            print("Binary")
    else:
        print("Not Binary")
        break
