'''
The task is to implement a function so as to print the sentence 
such that each word in the sentence is reversed.
A word is a combination of characters without any spaces.
'''

str = input()
words = str.split()
#print(words)
rev_word = []
for i in words:
    rev_word.append(i[::-1])
#print(rev_word)

rev_str = ' '.join(rev_word)
print(rev_str)