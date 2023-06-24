list1=[1,2,3]
list2=[1,3,2]
len=len(list1)
i=0
while i<len-2:
    list1.extend(list2)
    list1.sort()
    i=i+1
print(list1)    