# binary to decimal
# a=int(input("enter the number:"))
# i=0
# s=0
# while a>0:
#     b=a%10
#     s=s+b*2**i
#     a=a//10
#     i=i+1
# print(s)

# decimal to binary
# a=int(input("enter the number:"))
# len=len(str(a))
# i=0
# s=0
# while a>0:
#     c=a%2
#     a=a//28
#     s=s*10+c
# i=0
# while i>0:
#     m=s%10
#     i=i*10+m
#     s=s//10
# print(s)

# def binarySearch(array, x, low, high):
#     # Repeat until the pointers low and high meet each other
#     while low <= high:
#         mid = low + (high - low)//2
#         if array[mid] == x:
#             return mid
#         elif array[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x, 0, len(array)-1)
# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")
# 


# a=[5,8,2,10]
# b=2
# max=0
# min=a[0]
# for i in a:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# c=(max+min)//2
# print(c)
# if a[c] < b:  
#     min=c+19 
# elif a[c] > b:  
#     max =c - 1  
# else:
#     return c






   
# def a (b, n):  
#     max=0
#     min=b[0]
#     c=0
#     for i in b:
#         if i>max:
#             max=i
#         elif i<min:
#             min=i
#     while min <= max:  
#         # for get integer result   
#         c = (max+ min) // 2  
  
        # Check if n is present at mid   
        # if b[c] < n:  
        #     min = c + 1  
  
        # # If n is greater, compare to the right of mid   
        # elif b[c] > n:  
        #     max = c - 1  
  
        # If n is smaller, compared to the left of mid  
    #     else:  
    #         return c
    #         # element was not present in the list, return -1  
    # return -1  
  
  
# Initial list1  
# b= [5,2,9,6]  
# n = 2 
# # Function call   
# result = a (b, n)  
# if result != -1:  
#     print("Element is present at index", str(result))  
# else:  
#     print("Element is not present in list1")  


  



    
