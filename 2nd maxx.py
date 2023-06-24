a=[50,30,56,70,45,80]
i=0
s_max=0
max=0
while i<len(a):
    if a[i]>max:
      s_max=max
      max=a[i]
    elif a[i]>s_max:
      max=s_max 
      s_max=a[i]   
    i=i+1
print(s_max)      