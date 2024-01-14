'''Write a function called string_range that takes a single 
number and returns a string of its range. The string characters 
should be separated by dots(.) For example, if you pass 6 as 
an argument, your function should return 0.1.2.3.4.5.
'''
# ".".join(my_lst)


def string_range(n):
    
    s='.'.join([str(x) for x in range(0,n)])
    return s


n=int(input("Enter the range:"))
str=string_range(n)
print(str)