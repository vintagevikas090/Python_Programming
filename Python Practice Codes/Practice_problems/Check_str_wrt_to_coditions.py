def is_valid_string(st):
    if len(st)==0:
        return True
    if st[0]=='a':
        return is_valid_string(st[1:])
    if st.startswith('bb'):
        return is_valid_string(st[2:])
    return False

string = input()
result = is_valid_string(string)

if result:
    print('true')
else:
    print('false')