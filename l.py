# l=[[]]         
# n=3
# m=3
# i=0
# while i<n:
#     j=0
#     while j<m:
#         k=int(input("enter:"))
#         l[i].append(k)
#         j=j+1 
#     i=i+1 
# print(l)

l = []
i=0
n=int(input(" the number of list you want:"))
while i<n:  
    l.append([]) 
    j=0
    q=int(input("how many elements you want in the list:"))
    while j<q:
        k=int(input("enter the number to add in the list:"))
        l[i].append(k) 
        j=j+1 
    i=i+1
print(l)