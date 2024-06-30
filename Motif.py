
def Motif(S,T):
    pos = ''
    for i in range(len(S)):
        if S[i] == T[0]:
            if S[i:i+len(T)] == T:
                pos += str(i+1)+' '
    print (pos)


S = 'GATATATGCATATACTT'
T= 'ATAT'

Motif(S,T)