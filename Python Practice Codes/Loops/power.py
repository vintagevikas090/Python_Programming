base = int(input("Enter the base value: "))
power = int(input("Enter the power: "))
val = 1
for i in range(1,power+1):
    val = val*base
print(val)
