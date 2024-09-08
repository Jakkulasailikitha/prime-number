# a=int(input("enter the number:"))
# b=a
# s=0
# while b>0:
#     f=b%10
#     s=s+f
#     b=b//10
# if a==s**2:
#     print("special number")
# else:
#     print("not")
    

# a=int(input("enter the num1:"))
# b=int(input("enter the num2:"))
# if a <b:
#     print("first")
# elif a>b:
#     print("second")
# else:
#     print("any")

list=[4,5,5,5,3,8]
a=[]
for x in list:
    n=list.count(x)
    if n>2:
        if a.count(x)==0:
            c=x
print(c)

l=[1, 1, 1, 64, 23, 64, 22, 22, 22]
a=[]
for b in l:
    n=l.count(b)
    if n>2:
        if a.count(b)==0:
            a.append(b)
print(a)