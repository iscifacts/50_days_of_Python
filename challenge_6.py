'''Write a function called user_name that generates a username 
from the users email. The code should ask the user to input an 
email and the code should return everything before the @ sign 
as their user name. For example, if someone enters 
ben@gmail.com, the code should return ben as their user 
name'''
def user_name(email):
    n=len(email)
    s=""
    for i in range(0,n-1):
        if email[i]=='@':
            return s
        else:
            s=s+email[i]


email=input("Enter Your Mail id: ")
username=user_name(email)
print(username)