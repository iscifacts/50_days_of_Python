'''Write a function called count_dots. This function takes a 
string separated by dots as a parameter and counts how many 
dots are in the string. For example, h.e.l.p. should return 4
dots, and he.lp. should return 2 dots.'''

def count_dots(str1):
    n=len(str1)
    cnt=0
    for i in range(0,n):
        if str1[i]=='.':
            cnt=cnt + 1
    return cnt


str1=input("Enter String:")
ans=count_dots(str1)
print("The Number of dots are:",ans)