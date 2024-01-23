'''Write a function called sum_list with one parameter that takes 
a nested list of integers as an argument and returns the sum of 
the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
as an argument your function should return a sum of 33.'''

def sum_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        flattened_list.extend(sublist)
    return sum(flattened_list)


nested_list = [[2, 4, 5, 6],[2,3,5,6]]
result = sum_list(nested_list)
print(result)

