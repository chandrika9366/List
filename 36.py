list=['1', '2', '3', '4', '5', '6', '7', '8']
a=[]
#for i in range(0,len(list),2):
i=0
while i<len(list): 
    a.append(list[i]+list[i+1])
    i+=2
print(a)    