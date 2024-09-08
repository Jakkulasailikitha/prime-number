# a="applebanana"
# i=0
# b=""
# c=""
# j=1
# while i<len(a):
#     b=b+a[i]
#     i=i+2
# while j<len(a):
#     c=c+a[j]
#     j=j+2
# print(b,c)
    
# n=int(input("enter:"))
# i=0

a=[1,2,3,4,5,6,7]
i=0
b=[]
while i<len(a)-1:
    c=str(a[i]-a[i+1])
    b.append(c)
    i=i+1
print(b)