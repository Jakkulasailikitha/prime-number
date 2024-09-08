# print("Hello world")
# a=[1,"apple",8.5,[1,2,3]]
# b=[]
# c=[]
# d=[]
# i=0
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#     elif type(a[i])==str:
#         c.append(a[i])
#     else:
#         d.append(a[i])
#     i=i+1 
# print(b)
# print(c)
# print(d)
a="Today is thursday"
b=[]
a.split()
b=a.split()
i=0
s=[]
while i<len(b):
    j=0 
    c=0
    while j<len(a[i]):
        if a[i][j]!=",":
            c=c+1 
            j=j+1 
        s.append(c)
    i=i+1 
    print(s)