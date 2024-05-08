i = 0.05 #set i as the initial density
d = 0 #d represent the time in days
f = 0.9 #set f as the density threshold
while i <= f: #if the growing density lower than the threshold density, keep continuing the loops
    d += 1
    i *= 2
    print("the cell density on day"+str(d)+" is "+str(i))#print the final result until the loops stop
else:
    print("you should check lab on day",d-1)