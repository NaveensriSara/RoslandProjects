
#given a length of string, find the number of occurances each letter 

txt = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

A_count = 0
G_count = 0
C_count = 0
T_count = 0

for char in txt:
	if char == 'A':
		A_count += 1
		#print(A_count)
	elif char == 'T':
		T_count += 1
		#print(T_count)
	elif char == 'C':
		C_count += 1
		#print(C_count)
	else:
		G_count += 1
		#print(G_count)




print("A Count:", A_count )
print("G Count:", G_count )
print("C Count:", C_count )
print("T Count:", T_count )


