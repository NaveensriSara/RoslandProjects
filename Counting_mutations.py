#Counting point mutations 

str1= 'GAGCCTACTAACGGGAT'
str2= 'CATCGTAATGACGGCCT'

def Compare(str1,str2):
   
   count = 0
   for i in range(len(str1)):  # Loop through the indexes of the strings
        if str1[i] != str2[i]:  # Compare characters at index i in both strings
            count += 1  # Increment count if characters are different
    
    return count 


def Compare(str1, str2):
    if len(str1) != len(str2):
        print("Strings are of different lengths")
        return
    
    count = 0  # Initialize count to 0
    for i in range(len(str1)):  # Loop through the indexes of the strings
        if str1[i] != str2[i]:  # Compare characters at index i in both strings
            count += 1  # Increment count if characters are different
    
    return count