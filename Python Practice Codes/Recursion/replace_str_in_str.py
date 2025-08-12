# Replace 'pi' with 3.14

def ReplacePi(string):
    if len(string)==0 or len(string)==1:
        return string
    if string[0] == 'p' and string[1]=='i':
        smallerOutput = ReplacePi(string[2:])
        return '3.14'+smallerOutput
    else:
        smallerOutput = ReplacePi(string[1:])
        return string[0]+smallerOutput
    
print(ReplacePi('dflj;pifadpijadsfpiadfapi'))