# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
# a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# b=""
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b=b+a[i][j]
#         j=j+1
#     i=i+1
# print(b)
n=input("enter the string:")
if n.isupper():
    print("true")
elif n.islower() :
    print("false")
elif n.isdigit():
    print("false")
elif n.isalnum():
    print("False")
else:
    print("false")