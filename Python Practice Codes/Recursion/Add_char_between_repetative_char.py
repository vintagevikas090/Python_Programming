'''Given a string S, compute recursively a new string where identical chars 
that are adjacent in the original string are separated from each other by a "*".
'''

def pair_star(string):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]==string[1]:
        return string[0]+"*"+ pair_star(string[1:])
    else:
        return string[0]+ pair_star(string[1:])
st = input()
print(pair_star(st))