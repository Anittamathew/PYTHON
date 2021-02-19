c=0
n=0
m=1
nterms=int(input("no of terms"))
if(nterms<=0):
    print("enter positive")
else:
    print("Fibonacci series:")
    while(c<nterms):
        print(n,end=" ")
        p=n+m
        n=m
        m=p
        c=c+1
