'''
Program to create seperate files for 
multiplication tables from 2 to 20
'''
for i in range(1,21):
    with open(f"F:\Tables\Tables_Of_{i}.txt","w") as tables:        
        for j in range(1,11):
         tables.write(f"{i}  X {j} =  {i*j} \n")
        #break