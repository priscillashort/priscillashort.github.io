def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print('Welcome to the snow tire calculator. Please input the number of snow tires sold at your company this week and the number of people driving safer this winter will be printed')

x = input("Snow tires: ")
while is_number(x) == False:
    print("Oops! This is not a number.")
    x = input("Snow tires: ")
    
if is_number(x) == True:
    x = int(x)
    Result = x // 4
    print('The number of people driving safer this winter is', Result)
    input('Enter any key to exit: ')

