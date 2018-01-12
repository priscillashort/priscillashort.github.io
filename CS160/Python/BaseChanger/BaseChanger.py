# Base changer function
# Finished by Priscilla Short on 12-04-17

def convertSymToInt(sym):
    sym = sym.upper()
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

def convertFromDecimal(num, base):
    base = int(base)
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
    base = int(base)
    num = str(num)
    result = 0
    for i in range(1, len(num)+1):
        thisInt = num[i-1]
        mult = base**(len(num)-i)*convertSymToInt(thisInt)
        result = result + mult
    return result
    
def convertBaseToNewBase(num, curentBase, newBase):
    dec = convertToDecimal(num, curentBase)
    result = convertFromDecimal(dec, newBase)
    return result

# A short piece of code to test the functions using inputs and error handling
def testAllFunctions():
    play = 'YES'
    while play == 'YES':
        result1 = False
        result2 = False
        result3 = False
        while result1 == False:
            oldBase = input('Please enter the base you are converting from, using an integer: ')
            if oldBase.isdigit() == True:
                if int(oldBase) > 36 or int(oldBase) < 2:
                    print('You have entered an invalid base. Please limit your base from 2 to 36')
                else:
                    result1 = True
            else:
                print('You have not entered an integer for your base.')
                
        while result2 == False:
            newBase = input('Please enter the base you would like your number converted to, using an integer: ')
            if newBase.isdigit() == True:
                if int(newBase) > 36 or int(newBase) < 2:
                    print('You have entered an invalid base. Please limit your base from 2 to 36')
                else:
                    result2 = True
            else:
                print('You have not entered an integer for your base.')
                
        while result3 == False:
            num = input('Please enter a value to convert: ')
            count0 = 0
            for i in num:
                if i.isdigit() == False and i.isalpha() == False:
                    count0 = count0 + 1

            count = 0
            for i in num:
                if convertSymToInt(i) >= int(oldBase):
                    count = count + 1
                    
            if count > 0 or count0 > 0:
                print('Some of the characters in your number represent values higher than the base you are converting from. This is not a valid number.')
            
            if count == 0 and count0 == 0:
                result3 = True

        print(num, 'converted from base', oldBase, 'to base', newBase, 'is', convertBaseToNewBase(num, oldBase, newBase))
        play = input("Would you like to change another base? Type 'yes' to play and enter any other key to exit: ")
        play = play.upper()


testAllFunctions()

