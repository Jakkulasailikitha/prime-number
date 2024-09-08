# a=[123,234,178,198]
# i=0
# b=str(a[0])
# c=True
# while i<len(a):
#     d=str(a[i])
#     if b[0]!=d[0]:
#         c=False
#         break
#     i=i+1
# print(c)

a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(len(a)-1):
    n=a[i+1-a[i]]
    b.append(n)
print(b)
