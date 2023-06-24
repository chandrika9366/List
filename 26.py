#26. Our task is to print the element which occurs 3 consecutive times in a Python list.
list=[4,4,4,6,6,6,3,4,8]
len=len(list)
i=0
while i<len-2:
    if list[i]==list[i+1] and list[i+1]==list[i+2]:
        print(list[i])
    i=i+1            