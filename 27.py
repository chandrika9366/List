list1=[1,2,3]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j and j!=k and i!=k):
                print(list1[i],list1[j],list1[k])