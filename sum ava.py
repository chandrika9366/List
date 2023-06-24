#a=[23,14,56,12,19,9,15,25,31,42,43] 
a=[]
b=int(input("enter b"))
even_sum=0
odd_sum=0
i=0
while i<b:
    k=int(input("enter k"))
    a.append(k)
    if a[i]%2==0:
        even_sum+=a[i]     
    else:
        odd_sum+=a[i]
    i=i+1
ava_even=even_sum/i
ava_odd=odd_sum/i
print("even number",ava_even)
print("odd number",ava_odd)        