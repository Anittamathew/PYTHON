def fact(x):
    print("the factors of number",x, "are")
    for i in range(1,x+1):
        if(x%i==0):
            print(i)
num=int(input("enter a number:"))
fact(num)
