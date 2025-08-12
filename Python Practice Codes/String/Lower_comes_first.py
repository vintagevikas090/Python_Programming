#Arrange string characters such that lowercase letters should come first

s = "PYnAtivE"
for i in s:
    if(i.islower()):
        print(i, end="")
for i in s:
    if(i.isupper()):
        print(i, end="")