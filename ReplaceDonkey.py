
'''
User to write a sentence and prg will check if word 
donkey exist and replace it with ###### before writing to 
the output
'''
wordAdd = input("Enter a sentence : \n")

with open("F:\Output\CheckDonkey.txt","w") as addWord:
    addWord.write(wordAdd)

with open("F:\Output\CheckDonkey.txt") as checkDonkey:
    replaceDonkey = checkDonkey.read()
    if "donkey" in replaceDonkey.lower():
        with open("F:\Output\CheckDonkey.txt","w") as repDonkey:
            r = replaceDonkey.lower()
            repDonkey.write(r.replace("donkey", "######"))   
        print("donkey Replaced")
    else:
        print("No donkey in File")
        