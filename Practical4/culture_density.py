i = 0.05 #set initial density
d = 1 #time in days
print("the cell density on day"+str(d)+" is "+str(i))
f = 0.9 #set the density threshold
while i*2 <= f: #if the growing density lower than the threshold density, keep continuing the loops
    i *= 2
    d += 1
    print("the cell density on day"+str(d)+" is "+str(i))#print the final result until the loops stop
print("you should check lab on day",d)