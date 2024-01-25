'''Write a function called any_number that can receive any 
number of arguments (integers and floats) and return the 
average of those integers.'''

def any_number(*args):
       numbers = [num for num in args if isinstance(num, (int, float))]
       if not numbers:
              return None
       return sum(numbers)/len(numbers)

result=any_number(34,45,56,78,67)
print(result)