print(" Welcome to Mahik Calculator")

x= float(input("Enter your first Number: "))
y= float(input("Enter your second Number: "))
# we have four operators for agorithms
print(" For multiplication press 1")
print(" For Addition press 2")
print(" For Subtraction press 3")
print(" For Division press 4")
print(" For Exponential press 5")
# floor division actually means dividing a number and then round of the result to nearest whole number
print(" For Floor divison press 6")
# modulus operator is used to find the remainder of the division
print(" For Modulus press 7")
z= int(input())
if (z==1):

  print("The answer is :", x*y)
else:
    if (z==2):
        print("The answer is :",x+y)
if (z==3):
    print("The answer is :",x-y)
if (z==4): 
      print("The answer is :",x/y)
if (z==5):
      print("The answer is :",x**y)
if (z==6):
      print("The answer is :",x//y)
if (z==7):
      print("The answer is :",x%y)
else:
 print("Operator not found")
print("Thanks for using this Calculator")
