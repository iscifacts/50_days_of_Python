lst=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
    ele=input("Enter element:")
    lst.append(ele)
ans=[eval(i) for i in lst]
temp=sum(ans)
print(temp)