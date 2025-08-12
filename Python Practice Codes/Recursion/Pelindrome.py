# Check Pelindrome using recursion

def pelindrome(str):
    if len(str)<2:
        return True
    
    if str[0]==str[len(str)-1]:
        return pelindrome(str[1:len(str)-1])
    else:
        return False
    
string = input()
result = pelindrome(string)
if result:
    print("It's Pelindrome")
else:
    print("Not Pelindrome")