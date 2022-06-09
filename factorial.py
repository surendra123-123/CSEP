# Python program to find the factorial of a number provided by the user.
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)
num=int(input("Enter number to find factorial:"))
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",factorial(num))
