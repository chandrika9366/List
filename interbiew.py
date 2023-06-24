#a=[2,4,0,5,2,0,6,0]
a=[0,1,4,0,5,0,6]
i=0
len=len(a)
while i<len:
    if a[i]==0:
        a.append(a[i])
        a.remove(a[i])
    i=i+1
print(a)          