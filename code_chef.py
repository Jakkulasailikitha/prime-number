# a=[1,2,3,4,5]
# i=0 
# while i<len(a)-1:
#     if a[i+1]-a[i]==1 and a[i]<a[i+1]:
#         b="yes"
#     else:
#         b="no"
#     i=i+1 
# print(b)

# a=[1,7,3,8,2]
# i=0
# min=a[i]
# while i<len(a):
#     if min<a[i]:
#         min=a[i]
#     i=i+1 
# print(min)

# a=[3,1,4,1,5]
# i=0
# s=0
# f=0
# while i<len(a):
#     j=i+1 
#     while j<len(a):
#         f=a[i]*a[j]
#         s=s+f
#         print(s)
#         j=j+1
#     i=i+1 
# # print(s)


# n=5
# for x in range(1,n+1 ):
#     for y in range(1,n+1 ):
#         if(y==1 or x==y or x==n):
#             print( 
                
#                   "*",end=" ")
#         else:
#             print(" ",end=" ")
    # print()
# n=int(input("enter the number1:"))
# i=int(input("enter the number1:"))
# while n!=i:
#     if n>i:
#         n=n-i
#     else:
#         i=i-n 
# print(n)


i=1
while i<=5:
    j=1
    while j<=5:
        if j<=5-i:
            print(" ",end="")
        else:
            print("*",end="")
        j=j+1 
    i=i+1 
    print()