a=[1,2,3,[4,5,6],7,8,9]
i=0
b=[]
s=0
while i<len(a):
    if type(a[i])==list:
        sum=0
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        s=s+a[i]
    i=i+1
b.append(s)
b.append(sum)
print(b)

