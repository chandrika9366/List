a=int(input("enter a"))
b=[]
i=1
while i<=5:
    j=1
    c=[]
    b.append(i)
    while j<=10:
        k=i*j
        c.append(k)
        j+=1
    b.append(c)
    i+=1
print(b)    