"""Write a function called register_check that checks how many 
students are in school. The function takes a dictionary as a 
parameter. If the student is in school, the dictionary says yes. If 
the student is not in school, the dictionary says no. Your 
function should return the number of students in school. Use the 
dictionary below. Your function should return 3."""
def register_check(register):
    n=len(register)
    cnt=0
    for i in register.values():
        if i=='yes':
            cnt=cnt+1
    return cnt



register={'Ishita':'yes','Arpit': 'yes', 'Michael':'yes','John': 'no', 
 'Peter':'yes', 'Mary': 'yes'}
ans=register_check(register)
print(ans)