#Program to built a box of user defined size
n = int(input("No of lines you want : "))
for i in range(1,n+1):
    if (i ==1) or (i ==n):
        print("*" * n)       
    else:
        print ("*", ((n-4) * " "), "*")