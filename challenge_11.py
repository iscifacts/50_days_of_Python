'''Write a function called equal_strings. The function takes two 
strings as arguments and compares them. If the strings are equal 
(if they have the same characters and have equal length), it 
should return True, if they are not, it should return False. For 
example, love and evol should return True'''

def equal_strings(str1,str2):
    n1=len(str1)
    n2=len(str2)
   
    if n1!=n2:
        return False
    for char1,char2 in zip(str1,str2):
        if char1!=char2:
            return False
    return True


str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
ans=equal_strings(str1,str2)
print(ans)