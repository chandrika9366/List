list=[1,2,3,1,2,2]
i=0
list1=[]
while i<len(list):
    if list[i]not in list1:
       list1.append(list[i])
    i=i+1
print(list1)