# the out put should be:[[2, 1], 2, 3, [2, 4], 5, 1]
a=[1,1,2,3,4,4,5,1]
b=[]
i=0
while i<len(a)-1:
    c=1
    if a[i]==a[i+1]:
        c=c+1
        d=[c,a[i]]
        b.append(d)
        i=i+1
    else:
        b.append(a[i])
    i=i+1
b.append(a[-1])
print(b)
    