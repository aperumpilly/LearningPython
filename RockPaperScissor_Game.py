import random

def gameOutput(compNumber,yourNumber):
    print(f" Computer Selected {compNumber} and You Selected {yourNumber}")

def matchtheNumber(compNumber,yourNumber):
    if compNumber == 1:
         if yourNumber ==2:
             gameOutput(compNumber,yourNumber)
             print("You Win - ")    
             return "You Win"        
         elif yourNumber == 3:
             gameOutput(compNumber,yourNumber)
             print("You lost")
             return "You Lost"
         elif yourNumber == 1:
             gameOutput(compNumber,yourNumber)
             print("Both Selected same number")
             
    elif compNumber == 2:
             if yourNumber == 1:
                 gameOutput(compNumber,yourNumber)
                 print("You Lose")
                 return "You Lost"                
             elif yourNumber == 3:
                 gameOutput(compNumber,yourNumber)
                 print("You Win")
                 return "You Win"
             elif yourNumber == 2:
                  gameOutput(compNumber,yourNumber)
                  print("Both Selected same number")
               
    elif compNumber == 3:
            if yourNumber == 1:
                gameOutput(compNumber,yourNumber)
                print("You Win")
                return "You Win"
             
            elif yourNumber == 2:
                gameOutput(compNumber,yourNumber)
                print("You Lose")
                return "You Lost"
            elif yourNumber == 2:
                gameOutput(compNumber,yourNumber)
                print("Both Selected same number")
             
            #elif compNumber == yourNumber:
             #   gameOutput(compNumber,yourNumber)
                
    else:
        print("Some issue")
     #3
     #return compPoint,myPoint

howmanyRound= int(input("How many round to play : "))
for i in range(1,howmanyRound +1):
 print("*" * 60)
 print(f"            Round {i} \n 1-Stone, 2-Paper, 3-Scissor")
 yourNumber = int(input("Enter the number you want : "))
 if (yourNumber in range(1,4)): 
    compNumber = random.randint(1,4)
    #print(compNumber)
    matchtheNumber(compNumber, yourNumber) 
 else:
    print("Not a valid selection")
#print(f"{compPoint}, {myPoint}")
    

