list=[[1, 2, 4], [2, 4, 4], [1, 2]] 
b=[]
i=0
while i<len(list):
    c=0
    sum=0
    j=0
    while j<len(list):
        if len(list[j])>i:
            a=list[j][i]
            sum=sum+a
            c=c+1
        j=j+1 
    b.append(sum)
    i=i+1
print(b)        