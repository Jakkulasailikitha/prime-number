num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))
if num1 > num2:
    if num1 < num3:
        median = num1
    elif num2 > num3:
        median = num2
    else:
        median = num3
else:
    if num1 > num3:
        median = num1
    elif num2 < num3:
        median = num2
    else:
        median = num3
 
print("The median is", median)