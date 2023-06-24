name=input("enter name")
chr=('a','e','i','o','u')
i=0
while i<len(chr):
    if name[i]not in chr:
        print(name[i])
    else:
        print(name[i]) 
    i=i+1       
