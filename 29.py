list=[5, 6, [], 3, [], [],9]
i=0
new=[]
while i<len(list):
    if list[i]!=[]:
        new.append(list[i])
    i=i+1
print(new)
