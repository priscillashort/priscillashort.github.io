def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print("Hello, welcome to the gas milage calculator. For testing purposes, please try to input both numebrs and non numbers to see how the program reacts. Thank you!")
x = input("Please input the number of galons of gas used: ")
while is_number(x) == False:
    print("Oops! This is not a number.")
    x = input("Please input the number of galons of gas used: ")
while is_number(x) == True:
        y = input("Please input the number of miles traveled: ")
        if is_number(y) == True:
            print("Your gas milege is: ", float(y) / float(x))
            break
        else:
            print("Oops! This is not a number.")
