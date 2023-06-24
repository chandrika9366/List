num=[1, 1, 2, 3, 4, 4, 5, 1]                #"aaabbccdcnss"
y=[]
len=len(num)
i=0
while(i<len):
    count=0
    k=num[i]
    while i<len and num[i]==k:
        count=count+1
        i=i+1
    if(count>1):
        y.append([count,k])
    else:
        y.append(k) 
print(y)               