def percentFunc(marks):
    p = (sum(marks)/400 *100)
    return p
def printHello():
    print("Program is completed")

marks1 =[80,60,90,95]
marks2 = [88,85,82,80]
percentage1 =  percentFunc(marks1)
percentage2 = percentFunc(marks2)
print(percentage1, percentage2)
printHello()
#print (sum(marks1))