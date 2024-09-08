l=[[1,2,3],[2,3,4],[6,2,1,4]]
i=0
s=0
while i<len(l):
    j=0
    while j<len(l):
        a=l[i][j]
        s=s+a
        j=j+4
    i=i+1
print(s)