question=["1.how many continents are there?","what is the capital of india?","ng mei kaun se course padhaya jaata hai?"]
option=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.dehli"],["1.software engineering","2.counselling","3.tourism","4.agriculture"]]
solution=[3,4,1]
lifeline_option=[["1.four","2.seven"],["1.chandigarh","2.delhi"],["1.software","2.engineering","3.toursm"]]
lifeline_solution=[[2,2,1]]      
i=0
amount=0
while i<len(question):
    print(question[i])
    j=0 
    while j<len(option[i]):
        print(option[i][j])
        j+=1
        lifeline=input("aapko lifeline chahiyeh")
        if lifeline=="yes":
            c=0
            while c<len(lifeline_option[i]):
                print(lifeline_option[i])
                c+=1
            lifeline_solution=int(input("enter lifeline solution"))
            if lifeline_solution==lifeline_solution[i]:
                amount+=1
                print("sahi answer") 
            else:
                print("galat hain")
                break
        i+=1        