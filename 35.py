list=[1234, 122, 1984, 1372, 100]
len=len(list)
i=0
while i<len:
    x=(str(list[i])) 
    y=(str(list[i]))
    if (x[0]==y[0]):
        match=True 
    else:
        match=False                     
    i=i+1
print(match)    