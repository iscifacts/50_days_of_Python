'''Write a function called only_floats, which takes two 
 parameters a and b, and returns 2 if both arguments are floats,
 returns 1 if only one argument is a float, and returns 0 if neither 
argument is a float. If you pass (12.1, 23) as an argument, your 
function should return a 1.'''

def only_floats(a,b):
    if isinstance(a,float) and isinstance(b,float):
        print("2")
    elif isinstance(a,float) or isinstance(b,float):
        print("1")
    else:
        print("0")

a=23
b=12
only_floats(a,b)