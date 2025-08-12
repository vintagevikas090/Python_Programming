#Swap commas and dots in a String

s= "14, 625, 498.002"
for i in s:
    if i == ",":
        print(".", end="")
    elif i == ".":
        print(",", end="")
    else:
        print(i, end="")

