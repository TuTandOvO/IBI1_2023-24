#Some Simple Math
a = 40
b = 36
c = 30
d = a-b #The improvement from running only
e = b-c #The improvement from combine running and strength exercise
if d < e:
    print("use a combination of running and strength exercise is better")
elif e>d:
    print("only running is more effective")
else:
    print("running only and running combined strength exercise is the same")

#Booleans
X = True
Y = False
W = X ^ Y # W is true because because '^' means it would only be true when one of X and Y are true
print(W)