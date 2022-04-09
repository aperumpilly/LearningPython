#To get the maximum number from the list provided
num = int(input("Enter the number of values to compare : "))
a =[]
for i in range(num):
    intValue= int(input(f"Enter the {i+1} number  : "))
    a.append(intValue)
print(f"Out of {a} maximum is :" ,max(a))    