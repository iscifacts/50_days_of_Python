'''Create a function called my_discount. The function takes no 
arguments but asks the user to input the price and the 
discount (percentage) of the product. Once the user inputs the 
price and discount, it calculates the price after the discount. 
The function should return the price after the discount. For 
example, if the user enters 150 as price and 15% as the discount, 
your function should return 127.5.'''
def my_discount(price,Discount):
    profit=(Discount/100)*price
    amount=price-profit
    return amount





price=int(input("Enter Price: "))
Discount=int(input("Enter discount: "))
ans=my_discount(price,Discount)
print(ans)