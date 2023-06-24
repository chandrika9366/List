a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e_sum=0
o_sum=0
e_count=0
o_count=0
len=len(a)
while i<len:
    if a[i]%2==0:
        e_count+=1
        e_sum+=a[i]
    else:
        o_count+=1
        o_sum+=a[i]
    i=i+1
ava1= e_sum//i
ava2= o_sum//i
print("even count",e_count)
print("odd count",o_count) 
print("all of the count num",e_count+o_count) 
print("even sum",e_sum)
print("odd sum",o_sum)
print("all of the sum",e_sum+o_sum)
print("even ava",ava1)
print("odd ava",ava2)
print("ava all of the num",ava1+ava2)         