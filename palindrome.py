a=input("enter a")
i=int(len(a))-1
sum=""
while i>=0:
    sum=sum+a[i]
    i=i-1
if a==sum:
    print("palindrome") 
else:
    print("not palindrome")        