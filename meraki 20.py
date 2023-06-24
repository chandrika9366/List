student1=[78,76,94,86,88]
student2=[91,71,98,65]
student3=[95,45,78]
student4=[87,67,49,68,88]
total=student1+student2+student3+student4
len=len(total)
sum=0
i=0
while i<len:
    sum=total[i]+sum
    i=i+1
print("sum",sum)    