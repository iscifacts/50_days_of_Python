'''Write a function called capitalize. This function takes a string 
as an argument and capitalizes the first letter of each word. For 
example, i like learning becomes I Like Learning.'''


def capitalize(input_string):
   
    words = input_string.split()

    
    capitalized_words = [word.capitalize() for word in words]

    
    result_string = ' '.join(capitalized_words)

    return result_string


input_str = 'i like learning'
result = capitalize(input_str)
print(result)
