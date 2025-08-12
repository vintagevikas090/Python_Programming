'''Given a string S, you need to remove all the duplicates.
That means, the output string should contain each character only once.
The respective order of characters should remain same, as in the input string.'''

def uniqueChar(s): 
    # Write your code here
    freq = {}
    new_str = ""
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            new_str+=char
            freq[char]=1
    return new_str

# Main 
s=input() 
print(uniqueChar(s))