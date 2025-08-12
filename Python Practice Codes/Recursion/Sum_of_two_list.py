def sumOfTwoArrays(ARR1, N, ARR2, M, output):
    carry = 0  # Initialize carry to 0
    
    # Iterate through the arrays in reverse order and calculate the sum
    i = N - 1
    j = M - 1
    k = len(output) - 1
    
    while i >= 0 or j >= 0:
        # Calculate the sum of digits from both arrays and the carry
        if i >= 0:
            digit1 = ARR1[i]
        else:
            digit1 = 0
        
        if j >= 0:
            digit2 = ARR2[j]
        else:
            digit2 = 0
        
        # Calculate the sum of the digits and the carry
        digit_sum = digit1 + digit2 + carry
        output[k] = digit_sum % 10  # Store the last digit of the sum
        carry = digit_sum // 10  # Update the carry
        
        i -= 1
        j -= 1
        k -= 1
    
    # Handle any remaining carry
    if carry > 0:
        output[0] = carry

# Example usage
ARR1 = [6,9,8,5]  # Example array 1
ARR2 = [0]  # Example array 2

# Initialize the output array with zeros
output_size = max(len(ARR1), len(ARR2)) + 1
output = [0] * output_size

# Call the function to calculate the sum and store it in the output array
sumOfTwoArrays(ARR1, len(ARR1), ARR2, len(ARR2), output)

# The sum is now stored in the output array
# You can access the elements of the output array to get the result
print(output)
