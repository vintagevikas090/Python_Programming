def count_zero(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    if n % 10 == 0:
        return 1 + count_zero(n//10)
    else:
        return count_zero(n//10)
num = int(input())
print(count_zero(num))