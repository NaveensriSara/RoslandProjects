#Take the even lines of the following txt and document and remove them 
#Return the file with only the odd lines 

from numpy import array

#read text file 
file = open('randomLines.txt').readlines()

#import re
line = 1 #The count for the file 
for lines in file :
 #this lines is the actual lines in the file needs to be different 
 #than the count bc u are setting that earlier
	if line % 2 == 0:
		#lines.append(line.strip())
		print (lines)
	line += 1
#print(lines)
