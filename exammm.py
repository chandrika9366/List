# list=[4,5,6,3,9,6]
# list=sorted(list)
# print(list) 

# a="this is navgurukul"
# count=0
# i=0
# while i<len(a):
# #for i in range(len(a)):
#     if a[i]==" ":
#         count+=1
#     i+=1    
# print(count)        

a=int(input("enter a"))
count=0
i=0
while i<a-1:
#for i in range(a-1):
    if a%(i+1)==0:
        count+=i+1 
    i+=1       
if (count==a):
    print("perpect")
else:
    print("not")            