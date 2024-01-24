'''Write a function called user_name, that creates a username 
for the user. The function should ask a user to input their name. 
The function should then reverse the name and attach a 
randomly issued number between 0 to 9 at the end of the name. 
The function should return the username.'''
import random

def user_name():
    name=input("Enter Your Name:")
    name=name[::-1]
    num=random.randrange(0,10,1)
    user_name=name+str(num)
    return user_name

print(user_name())