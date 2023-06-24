list1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]  
len=len(list1)
c=[]
i=0
while i<len:
     d=list1[i]+list2[i]
     c.append(d)
     i=i+1
print(c)      