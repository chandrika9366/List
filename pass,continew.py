num=[1,3,2,3,1,0,1,3]
i=0
while i<len(num):
    pass
    if num[i]==0:
        count=i
        break
    elif num[i]%2==0:
        continue
    print(num[i])
    i+=1
print(count)    
