

#Count all letters, digits, and special symbols from a given string


s = "P@#yn26at^&i5ve"

char_count = 0
digit_count = 0
sym_count = 0
for i in s:
    if (i.isalpha()):
        char_count = char_count+1
    elif(i.isdigit()):
        digit_count = digit_count+1
    else:
        sym_count = sym_count+1

print("Total character: ", char_count)
print("Total digit: ", digit_count)
print("Total symbols: ", sym_count)

