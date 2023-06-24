a=int(input("enter a"))
i=1
b=[]
while i<=a:
    j=1
    c=[]
    b.append(i)
    while j<=5:
        c.append(j)
        j+=1
    b.append(c)
    i+=1
print(b)       
 
a=[1,2,[4,1],7,1,[4,5],9]
i=0
sum=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            sum+=a[i][j]
            j+=1
    else:
        sum+=a[i] 
    i+=1
print(sum)     

a="hi my name riya"
k=a.split()
k.insert(3,"is")    
print(k)     