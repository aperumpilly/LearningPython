from operator import truediv
from xmlrpc.client import boolean
a = 'Anish'
b =24
c = 19.03
d = True    
#Printing the values
print(a)
print(b)
print(c)
# d= 22
if (d == (not bool) ):
   print(d)
else:
    print("It is not boolean")
#Printing the types
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#typecasting  b value
print(str(b) + " is lucky number for Anish")
print(str(type(str(b))) + " is age of Anish")
print(b)
# #askName = input("What is your name ?")
# print(askName)
# print(type(askName))
print(type(b) ,type(c))

#format the number and MOD example
print(f"The remainder when {b} is divided by {c} is:", b%c)
print(b>c)

#Input 2 number and average it
f= input("Enter number 1: " )
g = input ("Enter number 2 : ")
print((int(f)+int(g))/2)
# Print the square of t F entered before
print (f"The square of {f} is :", int(f) * int(f))

#Printing various strings
b= 'Anish' #--> when it is a simple string
c = "Anish's" #--> when wanted to use ' inside string
d= ''' Anish"s''' #--> when wanted to use " inside string
print( b ,c ,d)
g = b + c # adding/concatetion 2 strings
print(g)
print(c[5]) # slicing the string
print(f"To print from 0 to 3 of {c}", c[0:3])
print(f"To print from 2 to 4 of {c}", c[2:4])
print(f"To print from 3 to 4 of {c}", c[3:4])

