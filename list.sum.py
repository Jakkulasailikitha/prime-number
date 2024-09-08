a=[12,34,56,78]
i=0
d=[]
while i<len(a):
    sum=0
    b=a[i]%10
    sum=sum+b
    e=a[i]//10
    c=sum+e
    d.append(c)
    i=i+1
print(d)