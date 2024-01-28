'''Write a function called make_tuples that takes two lists, 
equal lists, and combines them into a list of tuples. For 
example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
function should return [(1,5), (2,6), (3,7), (4,8)]'''

def make_tuples(list_a, list_b):
    
    if len(list_a) != len(list_b):
        raise ValueError("Lists must be of equal length")

    
    result = list(zip(list_a, list_b))
    return result


list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

result_tuples = make_tuples(list_a, list_b)
print(result_tuples)
