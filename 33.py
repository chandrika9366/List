list=[12,67,98,34]
k=[]
for i in list:
    sum=0
    for j in str(i):
        sum+=int(j)
    k.append(sum)
print(k)  