a=[1,2,3,6,5]
i=0
while i<len(a):
    j=a[2::-1]
    k=0
    while k<len(a):
        p=a[3:5]
        o=[j+p]
        k+=1
    i=i+1
print(o)                  

# same_type?
a="()"
if a=="()":
    print("true")
else:
    print("false")    