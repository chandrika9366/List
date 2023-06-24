# numbers=[2,7,9,11,3]
# numbers.reverse()
# print(numbers)

# a=[5,6,8,5,4]
# i=0
# while i<len(a):
#      a.sort()
#      a.reverse()
#      i+=1
# print(a)

a=[5,6,8,5,4]
i=0
while i<len(a):
     j=i
     while j<len(a):
          if a[i]>=a[j]:
               a[i],a[j]=a[j],a[i]
          j+=1 
     i+=1
print(a)         
# a=[5,6,8,5,4]
# i=0
# while i<len(a):
#      j=i
#      while j<len(a):
#           if a[i]<=a[j]:
#                a[i],a[j]=a[j],a[i]  
#           j+=1
#      i+=1     
# print(a)  
