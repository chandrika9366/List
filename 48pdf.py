list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
j=[]
#for i in range(0,len(list),3):
#    j.append(list[i:i+3])
#print(j)
i=0
while i<len(list):
    j.append(list[i:i+3])
    i=i+3
print(j)   