list=[6,1,3,5,6,3,1]
i=0
list1=[]
product=1
while i<len(list):
    if list[i]not in list1:
        list1.append(list[i])
        product=list1[i]*product
    i=i+1    
print('product',product)         