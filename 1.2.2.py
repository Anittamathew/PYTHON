list=[]
n=int(input("enter no of elements: "))
for i in range(0,n):
    v=int(input("enter the elements: "))
    if(v>100):
        list.append('over')
    else:
        list.append(v)
print(list)
