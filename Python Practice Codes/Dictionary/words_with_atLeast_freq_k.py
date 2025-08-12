def find_words_with_freq_atleast_k(words, k):
    freq = dict()
    for word in words:
        if not freq.get(word, None):
            freq[word] = 1
        else:
            freq[word] += 1

    ans = []
    for key in freq.keys():
        if freq[key] >= k:
            ans.append(key)
    return ans


li = ["cat", "dog", "elephant", "cat", "tiger", "dog"]
print(find_words_with_freq_atleast_k(li, 2))