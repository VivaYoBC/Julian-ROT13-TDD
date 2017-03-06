import sys

'''
	Basic source code for the ROT13 algorithm
	
	Assumptions made (not specified in the documentation, inferred by examples)
		1. The " " (space) character is passed as is (otherwise words don'tmake sense)
		2. The newline character ("\n") is ignored in the algorithm itself, but
		   passed as is ONLY in the algorithm for reading a complete file into memory,
		   so that paragraphs will make sense (no checking is made as to where the
		   newline is logically at the end of a paragraph or not)
		
	Magic numbers:
		65 -  ASCII for 'A'
		78 -  ASCII for 'N' 
		97 -  ASCII for 'a'
		110 - ASCII for 'n' 
		90 -  ASCII for 'Z
		122 - ASCII for 'z'
		
	Inputs: A string with 1 element which should be a letter of the English alphabet
		(upper or lower case), or a space
	
	Outputs: A number corresponding to the ASCII character of the input letter, or a space
	         If the input is not one of the specified, an empty string is returned
		
'''	

def rot13(y):
	inchar = ord(str(y))

	outchar = ""
	if inchar >= 65 and inchar < 78 or inchar >= 97 and inchar < 110:
		outchar = str(chr(inchar + 13)) 
	elif inchar >= 78 and inchar <= 90 or inchar >= 110 and inchar <= 122: 
		outchar = str(chr(inchar - 13))
	elif inchar == 32: outchar = " "
	
	return outchar
