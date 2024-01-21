'''Write a function called flat_list that takes one argument, a 
nested list. The function converts the nested list into a one-dimension list. For example [[2,4,5,6]] should return 
[2,4,5,6].'''
def flat_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        flattened_list.extend(sublist)
    return flattened_list


nested_list = [[2, 4, 5, 6]]
result = flat_list(nested_list)
print(result)

