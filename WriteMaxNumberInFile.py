newNumber = int(input("Enter the new Number : \n"))  #Get the new number frol console
with open("F:\MyNumberFile.txt") as f:   #Mode by default is Read
    existNumber = f.read()               # Read the file content

if int(newNumber) > int(existNumber):    
    with open("F:\MyNumberFile.txt",'w') as f:  #Write mode has to be explicitly written
        f.write(str(newNumber))
        print("Old number "+ str(existNumber) + " is replaced by New number " + str(newNumber))
else:
    print("Old number " + str(existNumber) + " is still bigger than New number " +str(newNumber))