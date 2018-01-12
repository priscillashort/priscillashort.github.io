def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print('Welcome to the loan payment calculator. Please input the rate per period, present value, and number of periods and the loan payment will be printed')

x = input("Rate per period as a percentage (eg. 8 for 8%): ")
while is_number(x) == False:
    print("Oops! This is not a number.")
    x = input("Rate per period as a percentage (eg. 8 for 8%): ")
y = input("Present Value: ")
while is_number(y) == False:
    print("Oops! This is not a number.")
    y = input("Present Value: ")
z = input("Number of periods: ")
while is_number(z) == False:
    print("Oops! This is not a number.")
    z = input("Number of periods: ")
    
if is_number(x) == True and is_number(y) == True and is_number(z) == True:
    x=float(x)/100
    y=float(y)
    z=float(z)
    Result = (x*y)/(1-(1+x)**-z)
    Result = float(Result)
    Result = round(Result,2)
    print('The loan payment is $' + str(Result))
    input('Enter any key to exit: ')

