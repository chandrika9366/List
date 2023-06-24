num=[1,7,3,7,4,5,6,3]
i=0   
num1=[]
while i<len(num):
    j=0
    count=0
    while j<len(num):
        if num[i]==num[j]:
            count+=1
            if count>=2:
                if num[i]in num1:
                    #num1.append(num[i])
                    pass
                else:
                  num1.append(num[i])
        j=j+1
    i+=1
print(num1)    
