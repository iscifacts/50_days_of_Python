'''Write two functions. The first function is called count_words
which takes a string of words and counts how many words are in 
the string. 
The second function called count_elements takes a string of 
words and counts how many elements are in the string. Do not 
count the whitespaces. The first function will return the number 
of words in a string and the second one will return the number 
of elements (less whitespace). If you pass I love learning, 
the count_words function should return 3 words and 
count_elements should return 13 elements'''

def count_words(str):
    sum=0
    for i in range(0,len(str)):
        if str[i]==' ':
            pass
        else:
            sum=sum+1
    return sum
def count_elements(str):
    sum=0
    for i in range(0,len(str)):
        if str[i]==' ':
            sum=sum+1
        else:
            pass
    return sum

str=input("Enter Your String")
words=count_words(str)
elements=count_elements(str)
print("The Number Of Words are ",words,"and number of elements are ",elements)