list1=[1,2,3]
a=[]
for i in range(0,3):
   for j in range(0,3):
      b=[]
      for k in range(0,3):
         if (i!=j and j!=k and i!=k):
            b.append(list1[i])
            b.append(list1[j])
            b.append(list1[k])
            a.append(b)
print(a)           


# num=[0,1]
# num1=[]
# num2=[]
# for i in range(0,2):
#   for j in range(0,2):
#      if (i!=j and j!=i):
#         num1.append(num[i])
#         num2.append(num[j])
# print([num1,num2])

# 2.dividend divisor multiple?
# a=int(input("enter dividend"))
# b=int(input("enter divisor"))
# i=0
# while i<=10:
#    k=a/b
#    i+=1
# print(k)   