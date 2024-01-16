'''Create a function called biggest_odd that takes a string of 
numbers and returns the biggest odd number in the list. For 
example, if you pass 23569 as an argument, your function 
should return 9. Use list comprehension'''

def biggest_odd(str):
    numbers = [int(digit) for digit in str]


    odd_numbers = [num for num in numbers if num % 2 != 0]

    
    return max(odd_numbers, default=None)
    

str=input("Enter string:")

ans=biggest_odd(str)
print(ans)