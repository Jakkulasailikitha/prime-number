# list=["Hello","mY", "WORLD"]

# new_list=[]
# for word in list:
#     new_list.append(word.lower())
# print (new_list)


# l=["R",["A"],["N"],["I"]]
# i=1
# a=""
# b=[]
# while i<len(l):
#     j=0 
#     while j<len(l[i]):
#         c=l[i][j].lower()
#         a=a+c
#         j=j+1
#     i=i+1
# c=(l[0][0]+a)
# b.append(c)
# print(b)

# 12345
# 22345
# 33345
# 44445
# 55555
# i=1
# while i<=5:
#     j=0
#     while j<=5:
#         if j>=1:
#             print(i+j,end="")
#         else:
#             print(j,end="")
#             j=j+1
#     i=i+1
#     print()
i=1
while i<=3:
    j=1
    while j<=3:
        if i==j:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    i=i+1
    print()