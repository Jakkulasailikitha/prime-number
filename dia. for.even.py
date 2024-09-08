# n=3
# for i in range (n,-(n),-1):
#     for j in range(1,abs(i)+1):
#         print(" ",end="")
#     for k in range(n,abs(i),-1):
#         print("* ",end="")
#     print()
# numb = [2, 3, 5,3, 7, 8,2,2]
# j=0
# sum=0
# for i in numb:
#     j=j+1

# for i in range(j-1):
#     for k in range(j-1):
#         if numb[k]>numb[k+1]:
#             numb[k],numb[k+1]=numb[k+1],numb[k]
# if j% 2 == 0:
#     median1 = numb[j//2]
#     median2 = numb[j//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = numb[j//2]
# print("the median of the list is",median)


# # Function to find the partition position
# def partition(array, low, high):
#     # choose the rightmost element as pivot
#     pivot = array[high]
 
#     # pointer for greater element
#     i = low - 1
 
#     # traverse through all elements
#     # compare each element with pivot
#     for j in range(low, high):
#         if array[j] <= pivot:
 
#             # If element smaller than pivot is found
#             # swap it with the greater element pointed by i
#             i = i + 1
 
#             # Swapping element at i with element at j
#             (array[i], array[j]) = (array[j], array[i])
 
#     # Swap the pivot element with the greater element specified by i
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
 
#     # Return the position from where partition is done
    # return i + 1
 
# function to perform quicksort
 
 
# def quickSort(array, low, high):
#     if low < high:
 
#         # Find pivot element such that
#         # element smaller than pivot are on the left
#         # element greater than pivot are on the right
#         pi = partition(array, low, high)
 
#         # Recursive call on the left of pivot
#         quickSort(array, low, pi - 1)
 
#         # Recursive call on the right of pivot
#         quickSort(array, pi + 1, high)
 
 
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
 
# size = len(data)
 
# quickSort(data, 0, size - 1)
 
# print('Sorted Array in Ascending Order:')
# print(data)




import json
user=input("enter signup or login:")
if user=="signup":
    user_name=input("enter the name")
    password1=input("enter the password1:")
    print("please confirm your password")
    password2=input("enter the password2:")
    if len(password1)>=1 and len(password1)<=16:
        if "@" in password1 or "#" in password1 or "$" in password1:
            if "A" or "z" in password1:
                if "0" or "9" in password1:
                    print("strong password")
                else:
                    print("week password")
            else:
                print("weekly password")
        else:
            print("nothing")
    else:
        print("wrong password")
    if password1==password2:
        pass
        with open ('Signup.json'):
            a=open('Signup.json',"r")
            data=json.load(a)
            for i in data["user"]:
                if i["username"]==user_name:
                    print("Already Exists")
                else:
                    dict={}
                    d={}
                    dict["username"]=user_name
                    dict["password"]=password1
                    d["Description"]=input("enter Description : ")
                    d["D.O.B"]=input("enter Date Of Birth : ")
                    d["Gender"]=input("enter your gender : ")
                    d["Hobbies"]=input("enter your Hobbies : ")
                    dict["Profile"]=d
                    a=data["user"]
                    a.append(dict)
                    f=open("Signup.json","w")
                    json.dump(data,f,indent=4)  
                    f.close()
                    print("Signup Succesfully")
                    break
    else:
        print("doesn't match")
elif user=="login":
    a=open("Signup.json","r")                 
    f=json.load(a)
    b=input("Enter your user name for login:")
    c=input("Enter your password for login:")
    for i in f["user"]:
        if b==i['username']:
            if c==i['password']:
                print("Login successful")
                print(i)
            else:
                print("Check your password")
                break
        else:
            print("Check your user_name")
            break
else:
    print("Your enter worng input ")
            
