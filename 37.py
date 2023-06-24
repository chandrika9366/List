list=[1,2,3,4,5,6]
list1=[]
n=len(list)
i=0
while i<n-1:
    list1.append([list[i],list[i]+1])
    i=i+1
print(list1)    