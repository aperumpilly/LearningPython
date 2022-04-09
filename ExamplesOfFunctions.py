""" """ def percentFunc(marks):
    p = (sum(marks)/400 *100)
    return p
def printHello(myName = "Sunny"): #Default parameter function
    print(f"{myName} is a good girl")
    print(myName)

marks1 =[80,60,90,95]
marks2 = [88,85,82,80]
percentage1 =  percentFunc(marks1)
percentage2 = percentFunc(marks2)
print(percentage1, percentage2)
#printHello()
printHello("Divya")

def factorial_rec(n):
    if n==1 or n==0:
        return 1
    return n* factorial_rec(n-1)

print(factorial_rec(int(marks1[1]))) # Take the first value of the List to iterate
#print(factorial_rec(5)) """

 





 """