a=int(input("enter a"))
b=str(a)
z=""
for i in b:
    if int(i)!=0:
        c=b.index(i)
        d=c-len(b)
        e=""
        for j in range(1,d*-1):
            e+="0"
        z+=i+e
        z+="+"
k=z[0:-1] 
print(k)           