'''Create a simple calculator. The calculator should be able to perform 
basic math operations, add, subtract, divide and multiply. The 
calculator should take input from users. The calculator should be 
able to handle ZeroDivisionError, NameError, and 
ValueError'''

a=input("Enter First Operand ")
b=input("Enter Second Operand ")
oper=input("Enter operation to perform: ")
if not(isinstance(a,int)) or not(isinstance(b,int)):
      raise ValueError
try:
    if(oper=='+'):
        print(int(a)+int(b))
    elif oper=='-':
        print(int(a)-int(b))
    elif oper=='*':
        print(int(a)*int(b))
    elif oper=='/':
        print(int(a)/int(b))
    else:
        print("Not a valid Operator")
except ValueError as ve:
        print("Value error")
except NameError as ne:
         print("Name error")
except ZeroDivisionError as ze:
         print("Zero Division Error")


