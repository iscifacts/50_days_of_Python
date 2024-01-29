'''Create three functions. The first called add_hash takes a string and 
adds a hash # between the words. The second function called 
add_underscore removes the hash (#) and replaces it with an 
underscore "_" The third function called remove_underscore,
removes the underscore and replaces it with nothing. if you pass 
Python as an argument for the three functions, and you call them at 
the same time '''

def add_hash(input_str):
    words = input_str.split()
    return '#'.join(words)

def add_underscore(input_str):
    return input_str.replace('#', '_')

def remove_underscore(input_str):
    return input_str.replace('_', '')

print(remove_underscore(add_underscore(add_hash('Python'))))