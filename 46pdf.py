list1=['0', '1', '2', '3', '4']
list2=['red', 'green', 'black', 'blue', 'white']
list3=['100', '200', '300', '400', '500']
len=len(list1)
i=0
k=[]
while i<len:
    name1=str(list1[i])
    name2=str(list2[i])
    name3=str(list3[i])
    p=name1+name2+name3
    k.append(p) 
    i=i+1    
print(k,end="")    
