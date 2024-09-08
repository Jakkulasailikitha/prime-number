a=[1,2,3,5,6,7,8]
i=0
b=[]
while i<len(a):
    c=a[i]**2
    d=c%10
    b.append(d)
    i=i+1
print(b)
