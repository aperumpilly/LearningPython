fruit = ['Apple','Kiwi','Guava','Orange']
#For Loop with break statement
fruit.append("Pineapple")
fruit.append("Chickoo")
print(fruit)
noFruit = input("From which fruit you do not want : \n")
print("Fruits you kept in basket are :")
for myFruit in fruit:    
    if myFruit == noFruit :
     break
    print(myFruit)
else:
    print("All done")
print("The Fruit which are skipped \n")
for leftFruit in range(fruit.index(noFruit) ,len(fruit)):        
        print(fruit[leftFruit])

