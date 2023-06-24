list=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k=2
b=[]
i=0
while i<len(list):
    a=list.count(i)
    if a>k and i not in b:
        b.append(i)
    i=i+1    
print(str(b))         