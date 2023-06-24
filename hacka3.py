s="aa"
p ="a*"
i=0
while i<len(s):
    j=0
    while j<len(p):
        if len(s)==len(p):
           match=True
        else:
           match=False
        j+=1   
    i=i+1  
print(match)             