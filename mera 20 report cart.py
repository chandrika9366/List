student_mark1=[78,76,94,86,88]
student_mark2=[91,71,98,65,76]
student_mark3=[95,45,78,52,49]
mixed=student_mark1+student_mark2+student_mark3
len=len(mixed)
total_mark=0
i=0
while i<len:
    total_mark=mixed[i]+total_mark
    i=i+1
print("total_mark",total_mark)  