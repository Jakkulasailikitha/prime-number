# i=1
# while i<=10:
#     print(i)
#     i=i+1


num=int(input("enter any nuber"))
i=1
c=0
while i<=num:
    if num%i==0:
        c+=1
    i=i+1

if c==2:
     print(num,"is prime number")
else:
    print(num,"is not a prime number")

