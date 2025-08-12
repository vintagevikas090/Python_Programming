
'''Remove special symbols / punctuation from a string'''
str1 = "/*Jon is @developer & musician"
for i in str1:
    if ((i.isalpha()) or i == " "):
        print(i, end="")