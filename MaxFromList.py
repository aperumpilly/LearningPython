#To get the maximum number from the list provided
num = int(input("Enter the number of values to compare : "))
a =[]
for i in range(num):
    intValue= int(input(f"Enter the {i+1} number  : "))
    a.append(intValue)
maxValue = max(a)
print(f"Out of {a} maximum is :" ,maxValue)    

print(f"The Fahrenheit conversion of {maxValue}°C is : ", (maxValue * 9/5) + 32)
#(0°C × 9/5) + 32 = 32°F
