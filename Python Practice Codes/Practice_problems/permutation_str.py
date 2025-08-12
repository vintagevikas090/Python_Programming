'''Permutations of each other
Two strings are said to be a permutation of each other
when either of the string's characters can be rearranged 
so that it becomes identical to the other one.'''

def permutation(str1, str2):
    for i in str1:
        if i in str2 and str1.count(i)==str2.count(i):
            pass
        else:
            return False
    return True

s1 = input()
s2 = input()
permutation(s1, s2)



#method 2

def are_permutation(st1, st2):
    if len(st1)!=len(st2):
        return False
    
    char_count_s1 = [0]*128
    char_count_s2 = [0]*128
    
    for i in st1:
        char_count_s1[ord(i)]+=1
    for j in st2:
        char_count_s2[ord(j)]+=1
        
    for k in range(128):
        if char_count_s1[k]!=char_count_s2[k]:
            return False
    return True

s1 = input()
s2 = input()
are_permutation(s1, s2)


# Code 3
def get_freq(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    return freq

def are_permutations(str1, str2):
    if len(str1) != len(str2):
        return False

    d1 = get_freq(str1)
    d2 = get_freq(str2)
    return d1 == d2
