def HighestOccuranceElement(string):
    char_count= [0]*128
    for char in string:
        char_count[ord(char)]+=1
    
    max_size = 0
    ch = None
    for i in string:
        if char_count[ord(i)]>max_size:
            max_size = char_count[ord(i)]
            ch = i
    return ch

s = "aaabbbdsfsfawegvljasdfaca "
print(HighestOccuranceElement(s))