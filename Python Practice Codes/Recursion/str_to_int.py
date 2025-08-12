def string_to_int(st):
    l = len(st)
    if l==0:
        return 0
    num = int(st[0]) *(10**(l-1))
    return num + string_to_int(st[1:])

string = input()
print(string_to_int(string))