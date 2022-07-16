import numpy  as np
myarr = np.array([[3,6,9,12,16],[4,8,12,16,20],[5,10,15,20,25],[6,12,18,24,30]])
x = len(myarr)
#print(x)
y =0
for i in myarr:    
    z =0
    for j in myarr[x-1]:
        print(myarr[y][z])
        z=z+1
    y=y+1    
    x=x-1

