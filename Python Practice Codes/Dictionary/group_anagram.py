'''
Anagrams are the words which can be rearranged to take the form of each other
eg.. 'ate' and 'eat' are anagram
'''
def get_freq_arr(word):
    freq = [0 for _ in range(26)]
    for i in range(len(word)):
        freq[ord(word[i]) - ord('a')] += 1
    return freq

def get_freq_str(freq):
    '''
    eg. convert 'abc' to 1#1#1
    '''
    str_freq = [str(num) for num in freq]
    return "$".join(str_freq)

def group_anagrams(arr):
    # required for the storage of words with string
    # eg. {1#1#1# : [abc, bca]}
    hashtable = dict()

    for word in arr:
        freq_arr = get_freq_arr(word)
        freq_str = get_freq_str(freq_arr)
        if freq_str in hashtable:
            # lst = hashtable[freq_str]
            # lst.append(word)
            hashtable[freq_str].append(word)
        else:
            hashtable[freq_str] = [word]

    res = []
    for value in hashtable.values():
        res.append(value)
    return res

# print('Enter the words(space seperated): ')
l = ["eat", "tea", "tan", "ate", "nat", "bat"]

output = group_anagrams(l)
print(output)
