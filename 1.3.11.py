def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
x=10
y=35
num=gcd(x,y)
print("GCD of ,'x',and,'y' is: ",num)