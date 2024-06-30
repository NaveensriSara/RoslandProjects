
#To find a substring's positions within a string 
def Motif(S,T):
    pos = ''
    #First start with first pos and as you go through S
    for i in range(len(S)):
        #check if it matches with the first letter of T
        if S[i] == T[0]:
            #see if the lenght of T is in S and matches
            if S[i:i+len(T)] == T:
                #add the position(add 1 for index) to postion variable and add a space 
                pos += str(i+1)+' '
    print (pos)

#Define and call
S = 'GATATATGCATATACTT'
T= 'ATAT'

Motif(S,T)