'''Create a function called average_calories that calculates the 
average calories intake of a user. The function should ask the user 
to input their calories intake for any number of days and once they 
hit done it should calculate and return the average intake.'''

def average_calories():
    lst=[]
    while True:
        try:
            calories=input("Enter calories for the day(Type Done if finished): ")
            if calories.lower()=='done':
                break
            else:
                calories=int(calories)
                lst.append(calories)
        except ValueError:
            print("Enter Valid Value")
    if lst:
        ans=sum(lst)/len(lst)
        return ans
    else:
        return 0

ans=average_calories()
print("The average intake of your calories is: ",ans)

        