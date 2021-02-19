x=int(input("enter a number"))
f=1
if(x<0):
    print("factorial not found for negative number")
else:
    for i in range(1,x+1):
        f=f*i
    print("factorial of",x,"is",f)