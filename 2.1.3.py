total=0
list=[]
n=int(input("enter no of terms:"))
for i in range(0,n):
    list.append(int(input("enter items:")))
print("list is",list)
print("length of list: ",len(list))
for i in range(0,len(list)):
    total=total+list[i]
print("total sum of list is ",total)