binary=[1,0,0,1,1,0,1,1]
rev=binary[-1::-1]
i=0
dec=0
while i<len(binary):
    if rev[i]==1:
        dec=dec+2**i
    i=i+1
print(dec)     

list=[1,1,0,1]
i=0
l=0-len(list)
power=0
decimal=0
while i>=l:
    if list[i]==1:
        a=list[i]
        c=2**power
        b=a*c
        decimal=decimal+b
    else:
        pass
    i-=1
    power+=1
print(decimal)        