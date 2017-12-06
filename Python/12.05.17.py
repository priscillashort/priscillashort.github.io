'''
def move1meter(distance, direction): #distance in intergers of meters - direction L or R
        left = 0
        right = 0
        count = 0
        if direction = 'L':
            while left != distance:
                left = count + 1
                left = left + left
                right = left / 2 + 1 + right
                '''

import random
#return the number of values in the hailstone sequence given n to start

def foo():
    return 3, 67

x, y = foo()

# pass in a maximum value and call hailstone(n) for 1..maximum n
#and return the n with the longest hailstone value

def maxHailstone(maxNum):
    nums = []
    for n in range(1, maxNum+1):
        count = hailstone(n)
        nums.append(count)
    maxValue = max(nums)
    return maxValue, nums.index(maxValue)


#Calculate the sequence of numbers in the hailstone sequence down to 1. Do not count the number n itself

def hailstone(n):
    return random.randint(1,1000)

#for i in range(10):
    #print(hailstone(0))

print(maxHailstone(100))
