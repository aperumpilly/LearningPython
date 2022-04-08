
'''# Program to greet all person name starting with D

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
''' 
# Program to check the prime number

i = int(input(" Enter the number : "))
isPrime = True
for prime in range(2,i):
    if(i%prime ==0):
        isPrime = False
        break
if isPrime == True:
    print( f"{i} is a prime number")
else:
    print(f"{i} is nota prime number")


  





