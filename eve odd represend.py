list=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[]
odd=[]
while i<len(list):
    if list[i]%2==0:
        even.append(list[i])   
    else:
        odd.append(list[i]) 
    i=i+1 
print("even=",even)
print("odd=",odd)                         