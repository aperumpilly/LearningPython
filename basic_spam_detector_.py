word = input("Enter the word to check : \n")
isSpam = False
if ("You are a winner" in word):
    isSpam = True
elif ("You have been selected" in word):
    isSpam = True
elif ("subscribe now to" in word):
    isSpam = True
elif("Will not believe your eyes" in word):
    isSpam = True
elif("Requires initial investment" in word):
    isSpam = True
elif("free credit card offers" in word):
    isSpam = True
   # print("Is this word a kind of spam : " , isSpam)
else:
    isSpam = False
print("Does this word sense you some spam : " , isSpam)






