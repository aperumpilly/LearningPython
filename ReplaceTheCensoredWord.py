'''
Program to check if the sentense has any
listed ceonsor word
'''
censorWords = ['idiot','foolish','dumb','rascal','moron']
checkWord = input("Enter the Word : \n")
for i in range(len(censorWords)):
    if censorWords[i] in str(checkWord):
         print(f"{checkWord} : has a censored word")
         break
    else:        
        if i == len(censorWords) -1:
            print(f"{checkWord} : does not have any censored word")
