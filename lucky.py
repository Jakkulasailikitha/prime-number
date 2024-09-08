# lucky : we have eleminate all the even position in it and the postition should be increment 
# than we have to cancel it
# n=int(input("enter the num:"))
# q=n
# i=2
# b="lucky number"
# while i<=n:
#     if q%i==0:
#         b="unlucky number"
#         break
#     else:
#         q=q-q//i
#     i=i+1 
# print(b)



i=1
while i<=5:
    j=5
    while j>=i:
        print("%",end="")
        j=j-1 
    i=i+1 
    print()
i=1
while i<=5:
    j=1
    while j<=i:
        print("%",end="")
        j=j+1 
    i=i+1 
    print()


rows = 7  # Number of rows in the pattern

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("%", end="")
    print()
