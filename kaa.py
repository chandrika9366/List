marks=["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks=0
i=0
while i<len(marks):
   total_marks=(total_marks + int(marks[i]))  
   i=i+1
print("total_marks",total_marks)