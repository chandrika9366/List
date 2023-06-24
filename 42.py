list=['a', 'b', 'c','d', 'e', 'f', 'g', 'h']
spec=3
x=[]
length=len(list)
#for i in range(length):
i=0
while i<length: 
    m=spec%length
    x.append(list[m])
    spec+=1
    i+=1
print(x)    