'''
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

'''
def matchingStrings(stringList, queries):
    # Write your code here
    freq = {}
    for string in stringList:
        if string not in freq:
            freq[string] = 1
        else:
            freq[string] += 1
         
    result = []
    for string in queries:
        result.append(freq.get(string, 0))
    return result
        
