list1=[3,1,5,7,89,4]
list2=[2,5,7,34]
if(len(list1)==len(list2)):
    print("lists are of same length")
else:
    print("lists are of different length")
if(sum(list1)==sum(list2)):
    print("lists are of same sum")
else:
    print('lists are of different sum')

n=any(value in list2 for value in list1)
if(n):
    print("common value occur in both list")
    print(set(list2).intersection(set(list1)))
else:
    print("no common value in both lists")