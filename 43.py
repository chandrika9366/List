list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x=20
n=4
i=n
while i<len(list):
    list.insert(i,x) 
    i+=n+1
print(list)         
