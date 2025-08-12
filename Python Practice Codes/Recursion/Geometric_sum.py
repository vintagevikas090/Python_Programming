# Finding Geometric Sum using Recursion

def geometricSum(k, n = 0):
    sum = 1/2**n
    if n>=k:
        return sum
    smallerOutput = geometricSum(k, n+1)
    return sum + smallerOutput

num = int(input())
geoSum = geometricSum(num)
print("{:.5f}".format(geoSum))