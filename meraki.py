student_mark= ["10", "32", "42", "65", "67", "89", "76", "38", "67"]#[36,30,54,67,35,70]
len=len(student_mark)
i=0
total_mark=0
while i<len:
    total_mark=int(student_mark[i]+total_mark)
    i=i+1
print("total_mark",(total_mark))    