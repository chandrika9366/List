char_list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
char=input("enter char")
i=0
count=0
while i<len(char_list):
    if char_list[i]==char:
        count+=1
    i+=1
print(count)        
# i=97
# c=122
# p=[] 
# while i<c:
#     j=0
#     sum=0
#     k=[]
#     while j<len(char_list):
#         if char_list[j]==chr(i):   
#            e=char_list[j]
#            sum=sum+1
#         j=j+1
#     if sum>0:
#         k.append(e)
#         k.append(sum)
#         p.append(k)
#     i=i+1
# print(p)                   