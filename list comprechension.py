# a=["suma","yapri"]
# b=[i for i in a if "suma"not in i]
# print(b)

# name=["chandrika","parista","kimpi"]
# new=[i for i in name if "a"in i]
# print(new)

a=[1,2,3,4]
i=0
while i<len(a):
    del a[0]
    i+=1
print(a)    