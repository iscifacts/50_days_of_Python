'''Create a function called all_the_same that takes one 
argument, a string, a list, or a tuple and checks if all the 
elements are the same. If the elements are the same, the function 
should return True. If not, it should return False. For example, 
[‘Mary’, ‘Mary’, ‘Mary’] should return True.'''

def all_the_same(lst):
    for i in range(0,len(lst)-1):
        if(lst[i]!=lst[i+1]):
            return False
    return True

lst=['mary','mary','mar']
ans=all_the_same(lst)
print(ans)

