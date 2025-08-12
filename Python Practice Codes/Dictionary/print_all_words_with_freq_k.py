
def All_words_with_freq_k(st):
    words = st.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    res = []
    for i in freq:
        if freq[i] == k:
            res.append(i)

    return res

string = input('Enter the string: ')
k = int(input('Enter the frequency: '))

output = All_words_with_freq_k(string)
print(*output)