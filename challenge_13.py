'''Write a function called your_vat. The function takes no 
parameter. The function asks the user to input the price of an 
item and VAT (vat should be a percentage). The function should 
return the price of the item plus VAT. If the price is 220 and, 
VAT is 15% your code should return a vat inclusive price of 253. 
Make sure that your code can handle ValueError. Ensure the 
code runs until valid numbers are entered. (hint: Your code 
should include a while loop).
'''
def your_vat():
        while(True):
            try:
                price=float(input("Enter Price:"))
                vat=float(input("Enter VAT: "))
                if(vat<0 and vat>100):
                     raise ValueError("VAT percentage must be between 0and 100")
                ans= price(1+ vat/100)
                print(f"The VAT inclusive price is: {ans:.2f}")
            except ValueError as ve:
                 print(f"Error: {ve}. Please enter valid numbers.")



result = your_vat()
print(f"Final result: {result:.2f}")



