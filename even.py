numbers=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
while i<len(numbers):
    if numbers[i]%2==0:
        even=even+numbers[i]
    else:
        odd=odd+numbers[i] 
    i=i+1
print("even",even) 
print("odd",odd)          