def Compare(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

string1 = 'GAGCCTACTAACGGGAT'
string2 = 'CATCGTAATGACGGCCT'
print(Compare(string1, string2))
