
# Program to greet all person name starting with D

nm = ["Ashish", "Dona", "Murli", "Danny", "Dulquer","Syam", "Amrit"]
""" for i in nm:
  if  i[0] =="D":
      print("Welcome ",i) """

# Program to get number from user and then show table
i=1
numb = int(input("Enter the number for multiplication : \n"))
while i<11 :        
        print(f"{i}   X  {numb} =" , i*numb )
        i +=1

""" # Program to check the prime number

i = int(input(" Enter the number : "))
isPrime = True
for prime in range(2,i):
    if(i%prime ==0):
        isPrime = False
        break
if isPrime == True:
    print( f"{i} is a prime number")
else:
    print(f"{i} is not a prime number")
 """

 #Program to print all the natural number till the number asked

inpNAt = int(input("Enter the number to list the Natural numbers ")   ) 
addNumb =0
for iLoop in range(1,inpNAt + 1):  
     addNumb += iLoop 
     if iLoop == inpNAt:
        print(iLoop, end = ',' )
        print(addNumb )
     else:
        print(iLoop, end = ',')
        print(addNumb, end = '|')

 #Program to print all the n factorial
fact =1
for iLoop in range(1,inpNAt+1):
    print(iLoop, " " ,fact, end = ' ')
    fact = fact*iLoop
    print(fact)    
 #Program to print star in old technqie, multiple loop   
incrNum =0
for iLoop in range(1,inpNAt+1):
    incrNum = incrNum + 1
    for inLoop in range(1,incrNum+1):
        print("*",end= ' ')
    print("\n")

 #Program to print star in new python technique

for iLoop in range(inpNAt):
    print("*" * (iLoop))
   
 #Program to print star in new python technique
for iLoop in range(inpNAt):
    print(" " * (inpNAt-iLoop -1),end=" ")
    print("*" * (2* iLoop +1),end=" ")
    print(" " * (inpNAt-iLoop -1))

#Program to built a box of user defined size
n = int(input("No of lines you want : "))
for i in range(1,n+1):
    if (i ==1) or (i ==n):
        print("*" * n)       
    else:
        print ("*", ((n-4) * " "), "*")

