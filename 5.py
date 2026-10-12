n=int(input("enter a positive number"))
count=0

for i in range(1,n+1):
    if n%i==0:
        count=count+1
print("number of factors:",count)
if count>2:
    print(f"{n} has more than two factor")
else:
    print(f"{n} has only two factor")
    
        
    