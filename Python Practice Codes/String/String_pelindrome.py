
#string pelindrome


s = input("Enter a string: ")
if s[::]==s[::-1]:
    print("pelindrome")
else:
    print("Not pelindrome")