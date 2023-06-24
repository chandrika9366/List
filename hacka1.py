num=[2,7,11,15]
i=0
target=9
while i<len(num):
    j=1
    while j<len(num):
        if target==num[i]+num[j]:
           p=[i,j] 
        j+=1
    i+=1
print(p)    