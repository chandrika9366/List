str= "https://www.w3schools.com/python/python_lists_add.asp"
list=['.com', '.edu', '.tv']
num=False
n = len(list)
i=0
while(i<n):
    if(str.find(list[i])!=-1):
        num=True
    i=i+1
print(num)

# list=['.com', '.edu', '.tv']
# i=0
# a="https://www.w3schools.com/python/python_lists_add.asp"
# while i<len(list):
#     if list[i]==a:
#         match=True
#     else:
#         match=False
#     i=i+1
# print(match)
            