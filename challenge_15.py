'''Write a function called same_in_reverse that takes a string 
and checks if the string reads the same in reverse. If it is the 
same, the code should return True if not, it should return False. 
For example, dad should return True, because it reads the 
same in reverse.'''

def same_in_reverse(str):
    str2=str[::-1]
    if str2==str:
        return True
    return False
str=input("Enter Your string: ")
ans=same_in_reverse(str)
print(ans)