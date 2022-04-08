
#Program for reverse multiplication using while as well as FOR loops
n = int( input("Enter multiplication number to be reverse : "))
print("*****Using FOR LOOP***** \n")
for i in range(-10, 0):
    print ( f"{n} X {-i} = { -i*n } \n" )

print("*****Using WHILE LOOP***** \n")
i = 10
while i > 0:

    #print (n , " X ", i,i*n)
    print(f"{i} X {n} = ",i*n)
    i -= 1