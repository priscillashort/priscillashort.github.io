def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print('Welcome to the largest number tool. Please input three numbers and the largest of the numbers will be printed')

x = input("First number: ")
while is_number(x) == False:
    print("Oops! This is not a number.")
    x = input("First number: ")
y = input("Second number: ")
while is_number(y) == False:
    print("Oops! This is not a number.")
    y = input("Second number: ")
z = input("Third number: ")
while is_number(z) == False:
    print("Oops! This is not a number.")
    z = input("Third number: ")
    
if is_number(x) == True and is_number(y) == True and is_number(z) == True:
    Result = max(int(x), int(y), int(z))
    print('The largest number is ', Result)
    input('Enter any key to exit: ')

