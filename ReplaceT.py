#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by 
#replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

#solution is done by going through each letter and appending it to string then when i == t replace it 
str = "GATGGAACTTGACTACGTAAATT"

#Solution #1
#print(str.replace("T","U"))


#going through a list with for loop using .replace()
#solution 2
new_str = []

for i in str:
	if i == "T":

		j=i.replace("T","U")
		new_str.append(j)
	else: 

		new_str.append(i)

print (new_str)


# 3rd solution using function the more effecient way with the help of chatGPT

def replace_char(start_str,changeChar,newLetter):
#create the function with starting input, what letter I want to change and the letter to change to
	new_string=""
	#if you define the string that u will use outside the function,
	#you can call the funtion later. A communicator 
	for char in start_str:
	#iterate
		if char === changeChar:
		#if that character in that iteration equals the target
			newLetter += newLetter
			#modify the letter
		else:
			newLetter += char
			#continue to the next char 

	return newLetter
	#return for the sake of the for loop to end the call function 


#now need to come up with new variable names that was used
#in the fucntion call at the top
orgString = "ATGCATGTGACGTAGCT"

replaceLetter = "T"

changeLetter = "U"
#now call the function that u used the communicator then use the function name 
new_string = replace_char(orgString,replaceLetter,changeLetter)

#print the comminucator now with the changes

print(new_string)

