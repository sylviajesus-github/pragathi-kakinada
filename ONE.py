#GET list of NO.S as INPUT, RETURN THR product if the product less than 750
#Else return the SUM
n=list(map(int,input("Enter").split()))
print(n)

x=1
y=0
for i in n:
    x=x*i
    y=y+i
if x<=750:
    print("prod",x)
else:
    print("Sum",y)

 
