# Replace Characters in a string

def replace(st, a, b):
    l = len(st)
    new_str = ""
    if l == 0:
        return st
    smallOutput = replace(st[1:], a, b)
    if st[0]==a:
        return b +smallOutput
    else:
        return st[0]+smallOutput

string = 'apple'
print(replace(string, 'a', 'b'))