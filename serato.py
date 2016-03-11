#SERATO, Mike Edward C.
#2013-10561
#CMSC 128 AB-1L

def getHammingDistance(str1, str2):							#counts the number of characters that are not the same per index
	if len(str1) != len(str2): 								#checks if both strings have the same length
		return "Error! Strings are not equal!"
	else: 
		distance = 0
		
		for i in range(0, len(str1)):						#checks every character of both string
			if str1[i] != str2[i]:							#checks if the character of the index is not the same
				distance += 1
		
		return distance		
		
def countSubstrPattern(original, pattern):					#counts the number of times a pattern can be found in the original string
	substr = 1												#this checks if the characters of the substring is consistently found
	count = 0	
	
	for i in range(0, len(original)-len(pattern)+1):		#loops until the length of pattern string
		for j in range(0, len(pattern)):
			if original[i+j] != pattern[j]:
				substr = 0 
		
		if substr != 0:										#goes here if the substring is found
			count += 1
		else:
			substr = 1										#initializes the substr again to 1
			
	return count

def isValidString(str, alphabet):							#checks if all the characters of a string is found in the given alphabet
	for i in range(0, len(str)):
		if str[i] not in alphabet:							#checks if the character is in the alphabet
			return "False"
			
	return "True"
				
def getSkew(str, n):										#gets the difference between number of Gs and number of Cs
	ccount = 0
	gcount = 0
	
	for i in range(0, n):									#checks all the characters of string
		if str[i] == "G":
			gcount += 1
		elif str[i] == "C":
			ccount += 1
	
	return gcount - ccount									#gets the difference between the two variables
	
def getMaxSkewN(str, n):									#gets the maximum among the skews 
	skews = []												#initializes an empty string where the skews will be stored
	
	for i in range(0, n):
		skews.insert(i, getSkew(str, i+1))					#calls the getSkew function and insert it to the list
	
	return max(skews)										
	
def getMinSkewN(str, n):									#gets the minimum among the skews
	skews = []												#initializes an empty string where the skews will be stored
	
	for i in range(0, n):
		skews.insert(i, getSkew(str, i+1))					#calls the getSkew function and insert it to the list
	
	return min(skews)
	
#print(getHammingDistance("AACCTT", "GGCCTT"))				#sample values for each function
#print(countSubstrPattern("AATATATAGG", "GG"))
#print(isValidString("AAGGCTATGC", "ACGT"))
#print(getSkew("GGCCAC", 1))
#print(getMaxSkewN("GGCCAC", 1))
#print(getMinSkewN("GGCCAC", 1))
