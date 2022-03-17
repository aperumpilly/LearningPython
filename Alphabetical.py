#used random module to add with Alphabet
import random
def alphabetical(words):
	number1 =  random.random()
	print(words + " " + str(number1)  )
	return ','.join(sorted(words.split(',')))	
alphabetical("Anish")
	

