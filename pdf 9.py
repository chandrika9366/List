a=[1,27,14,2,41,58,94,87]
i=0
max=0
s_max=0
third_max=0
while i<len(a):
    if a[i]>max:
        s_max=max
        max=a[i]
    elif a[i]>s_max:
        third_max=s_max
        s_max=a[i]
    elif a[i]>third_max:
        third_max=s_max
        third_max=a[i]
    i=i+1
print("first max",max)
print("second max",s_max)
print("thirt max",third_max)