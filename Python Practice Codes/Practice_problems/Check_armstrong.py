'''Check Armstrong
An Armstrong number is a number (with 'k' digits) 
such that the sum of its digits raised to 'kth' power is equal to the number itself. 
For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371. '''

n = int(input())
digits = len(str(n))
sum = 0
for i in str(n):
    sum = sum+(int(i)**digits)

if (n==sum):
    print("true")
else:
    print("false")

### Method 2
def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number%10)
        number = number//10
    return digits

def check_armstrong_number(num):
    if num == 0 or num == 1:
        return True

    digits = get_digits(num)
    n = len(digits)
    sum_value = 0
    for digit in digits:
        sum_value += digit**n

    return num == sum_value
