# Base changer function
# Written by Priscilla Short on 11-29-17

def convertSym(sym):
    ordVal = ord(sym)
    if ordVal in range(48, 58):
        result = ordVal - 48
    else:
        result = ordVal - 55
    return result

def convertIntToSym(num):
    if num in range(0,10):
        sym = chr(num + 48)
    else:
        sym = chr(num + 55)
    return sym

# Base Changer function - This should work for any interger converted to any interger base
def changeBase(num, base):
    if type(num) != int or type(base) != int:
        return 'You have not entered intergers for your arguements. Please only enter intergers.'
    divide = 'place holder'
    result = []
    while divide != 0:
        divide = num // base
        remain = num % base
        remain = convertIntToSym(remain)
        result.append(str(remain))
        num = divide
    result.reverse()
    result = ''.join(result)
    return result

def convertToDecimal(num, base):
    '''
    if type(num) != int or type(base) != int:
        return 'You have not entered intergers for your arguements. Please only enter intergers.'
    '''
    result = 0
    #num = [int(i) for i in str(num)]
    for i in range(1, len(num)+1):
        thisInt = num[i-1]
        mult = base**(len(num)-i)*convertSym(thisInt)
        result = result + mult
    return result

'''
#Peter's function
def convertToDecimal(startNum, startBase):
    powOfx = len(startNum) - 1
    sumVals = 0
    for ch in startNum:
        power = startBase**powOfx
        partialNum = int(ch) * power
        sumVals = sumVals + partialNum
        powOfx = powOfx - 1
    return sumVals
'''
    

def convertBaseToNewBase(num, oldbase, newbase):
    pass

def test():
    print(convertSym('0') == 0)
    print(convertSym('1') == 1)
    print(convertSym('A') == 10)
    print(convertSym('Z') == 35)
    print(convertIntToSym(0) == '0')
    print(convertIntToSym(9) == '9')
    print(convertIntToSym(10) == 'A')
    print(convertIntToSym(15) == 'F')
    print(convertIntToSym(35) == 'Z')

def mainOfOrig():
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
    print(convertToDecimal(changeBase(decNum, baseNum), baseNum))

test()
mainOfOrig()

