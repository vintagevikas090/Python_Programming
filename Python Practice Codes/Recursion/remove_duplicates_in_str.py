# Remove Duplicates Recursively

def RemoveConsecutiveDup(st):
    if len(st)==0 or len(st)==1:
        return st
    if st[0] == st[1]:
        return RemoveConsecutiveDup(st[1:])
    else:
        return st[0]+ RemoveConsecutiveDup(st[1:])
print(RemoveConsecutiveDup('xxxyyyzwwzzz'))