# start=int(input("enter start"))
# end=int(input("enter end"))
# for i in range(start,end+1):
#    if i<0:
#       print(i,end=",") 
#start=[-4,5]
start=int(input("enter start"))
end=int(input("enter end"))
while start<end:
    if start<0:
        print(start,end="")
    start=start+1   