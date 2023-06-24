# grocery_list=["flour","cheese","carrots"]
# i=0
# while i<len(grocery_list):
#     print(i,grocery_list[i],)
#     i=i+1

a=[1,7,[7,7],[4,3,5],"6"]
i=0
k=[]
while i<len(a):
    p=0
    while p<len(a):
        k.append(a[i][p])
        p+=1
    i+=1
print(k)        