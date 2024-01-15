'''Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the 
difference between the largest even number in the list and the 
smallest odd number in the list. For example, if you pass 
[1,2,4,6] as an argument the function should return 6 -1= 5'''

def odd_even(numbers,n):
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

   
    max_even = max(even_numbers) if even_numbers else float('-inf')
    min_odd = min(odd_numbers) if odd_numbers else float('inf')

  
    difference = max_even - min_odd

    return difference
    

lst=[]
n=int(input("Enter Number of elements:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

ans=odd_even(lst,n)
print(ans)