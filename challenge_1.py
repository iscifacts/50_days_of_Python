"""Write a function called divide_or_square that takes one 
argument (a number), and returns the square root of the number 
if it is divisible by 5, returns its remainder if it is not divisible by 
5. For example, if you pass 10 as an argument, then your function 
should return 3.16 as the square root."""


import math
#function to calculate values
def divide_or_square(a):
    if a%5!=0:
        return a%5
    else:
        return (math.sqrt(a))
        

a=int(input("enter a Number:"))
ans=divide_or_square(a)

print("Your answer is {}" ,ans)