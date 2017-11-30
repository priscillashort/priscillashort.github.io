# Base changer function
# Written by Priscilla Short on 11-29-17

# Base Changer function - This should work for any interger converted to any interger base
def changeBase(num, base):
    if type(num) != int or type(base) != int:
        return 'You have not entered intergers for your arguements. Please only enter intergers.'
    divide = 'place holder'
    result = []
    while divide != 0:
        divide = num // base
        remain = num % base
        result.append(str(remain))
        num = divide
    result.reverse()
    result = ''.join(result)
    return result

# A short piece of code to use the function using inputs and error handling
result1 = 'False'
result2 = 'False'
while result1 == 'False' or result2 == 'False':
    decNum = input('Please enter a decimal interger to convert: ')
    baseNum = input('Please enter the base you would like your number converted to, using an interger: ')
    try:
        int(decNum)
    except ValueError:
        print('You have not entered an interger for your number to convert.')
        result1 = 'False'
    else:
        result1 = 'True'
    try:
        int(baseNum)
    except ValueError:
        print('You have not entered an interger for your base.')
        result2 = 'False'
    else:
        result2 = 'True'
decNum = int(decNum)
baseNum = int(baseNum)
print(decNum, 'in base', baseNum, 'is', changeBase(decNum, baseNum))
