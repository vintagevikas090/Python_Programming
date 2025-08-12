def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)
n = int(input("Power: "))
base = int(input("Base: "))
print(power(base, n))