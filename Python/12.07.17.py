# Robot Treasure Hunt
# Written by Priscilla Short on 12.06.17
import math

def movement(distance, direction, function):    #distance = intergers of meters
    if direction == 'R':                        #direction = L or R for left or right
        return ifright(distance, direction, function)
    if direction == 'L':
        return ifleft(distance, direction, function)

def ifright(distance, direction, function):
    left = 0
    right = 0
    addleft = 0
    addright = 0
    add1 = function(addright, -1, 0)
    add2 = 0
    while (addright / 2) < distance:
        addright = function(addright, add1, add2)
        if addright >= distance:
            dif = addright - distance
            addright = addright - dif
            right = right + addright
            break
        addright = addright * 2
        right = right + addright
        add2 = add2 + 1
        addleft = function(addleft, add1, add2)
        addleft = addleft * 2
        left = left + addleft
        add1 = add1 + 1
    return int(left + right)

def ifleft(distance, direction, function):
    left = 0
    right = 0
    addleft = 0
    addright = 0
    add1 = function(addright, -1, 0)
    add2 = 0
    while (addleft / 2) < distance:
        addright = function(addright, add1, add2)
        addright = addright * 2
        right = right + addright
        add2 = add2 + 1
        addleft = function(addleft, add1, add2)
        if addleft >= distance:
            dif = addleft - distance
            addleft = addleft - dif
            left = left + addleft
            break
        addleft = addleft * 2
        left = left + addleft
        add1 = add1 + 1
    return int(left + right)


def AandB(add, num1, num2):
    if num1 >= 0:
        result = (add / 2) + num1 + num2
        return result
    return 1

def twotox(add, num1, num2):
    if num1 >= 0:
        result = 2**(num2 + num1)
        return result
    return 0

def twotolog(add, num1, num2):
    if num1 >= 0:
        result = 2**(math.log10(num1 + num2))
        return result
    return 1

def tentox(add, num1, num2):
    if num1 >= 0:
        result = 10**(num2 + num1)
        return result
    return 0

def testvalues():
    functions = [tentox, twotox, AandB, twotolog]
    direction = input('Please input a direction. ONLY R or L: ')
    direction = direction.upper()
    values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    for j in values:
        print('Total distance traveled when energy is', j, 'meters away:')
        alg = 1
        for i in functions:
            print('Algorithm', alg, '=', movement(j, direction, i))
            alg = alg + 1

testvalues()
