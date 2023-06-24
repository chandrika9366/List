student_mark1=[78,76,94,86,88]
student_mark2=[91,71,98,65]
student_mark3=[95,45,78]
mixed=student_mark1+student_mark2+student_mark3
len=len(mixed)
sum=0
i=0
while i<len:
    sum=mixed[i]+sum
    i=i+1
print("sum",sum)    