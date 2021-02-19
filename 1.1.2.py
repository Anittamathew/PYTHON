list=[]
n= int(input("enter the no of elements"))
for i in range(0,n):
    list.append(int(input("enter the integer:")))
print("printing positive integers:")
for i in list:
    if(i>0):
        print(i,end=" ")