a=[1,2,3,4,5]
b=[]
i=0
while i<len(a):
    c=a[i]**2
    d=c%10
    b.append(d)
    i=i+1
print(b)

