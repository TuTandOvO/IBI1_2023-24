i = 0.05 #set i as the initial density
d = 1 #d represent the time in days
print("the cell density on day"+str(d)+" is "+str(i))
f = 0.9 #set f as the density threshold
while i <= f: #if the growing density lower than the threshold density, keep continuing the loops
    i *= 2
    d += 1
    if i > 1:#the cell density maybe cannot beyond 1.0
        print("the cell desity on day6 is 1.0")
        break
    print("the cell density on day"+str(d)+" is "+str(i))#print the final result until the loops stop
print("you should check lab on day",d)