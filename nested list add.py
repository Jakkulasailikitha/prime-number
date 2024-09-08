


l=[[1,2,3],[5,6,7],[7,2,3]]
i=0
a=[]
while i<len(l):
    j=0
    sum=0
    while j<len(l[i]):
        sum=sum+l[j][i]
        j=j+1
    a.append(sum)
    i=i+1
print(a)
# # str = "Rohan"  
# # str2 = "ab"  
# # # Calling function    
# # str2 = str.join(str2)    
# # # Displaying result    
# # print(str2) 

# numbers=[1,8,6,4,3,9,0]
# i=0
# max=0
# sec_max=0
# third_max=0
# while i<len(numbers):
#     if numbers[i]>max:
#         third_max=sec_max
#         sec_max=max
#         max=numbers[i]
#     elif numbers[i]>sec_max:
#         third_max=sec_max
#         sec_max=numbers[i]
#     elif numbers[i]>third_max:
#         third_max=numbers[i]
#     i=i+1
# print(max)
# print(sec_max)
# print(third_max)
# def convertToBinary(n):
#    if n > 1:
#        convertToBinary(n//2)
#    print(n % 2,end = '')

# # decimal number
# dec = 34

# convertToBinary(dec)
# print()

# a=int(input("enter the number:"))
# b=[]
# while a!=0:
#     r=a%2
#     b.append(r)
#     a=a//2
# b.reverse()
# for i in b:
#     print(i,end="")

# def word(user):
#     count={}
#     for x in  user:
#         count[x]=user.count(x)
#     return count
# user=input("enter the string here:")
# print(word(user))
# "string" in "substring"
# "string" not in "substring"

