list1 = [2, -7, 5, -64, -14]
positive=0
nagative=0
i=0
while i<len(list1):
    if list1[i]>=0:
        positive+=1
    else:
        nagative+=1
    i=i+1
print("positive",positive) 
print("nagative",nagative)           
