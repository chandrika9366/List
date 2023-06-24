list = [1, 2, 2, 5, 8, 4, 4, 8]
len=len(list)
list1=[]
i=0
while i<len:
    if list[i]not in list1:
        list1.append(list[i])
    i=i+1
print(list1)    