"""
   Hangman
     Plays a basic game of hangman
    
   Author:  JJ Programmer
   Version: 0.01
   Date:    11/07/2017
"""

import random

def makeArt():
    art = []
    art.append('         +---------+') 
    art.append('         |         |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append(' ------------------+')
    return art

def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 4 and len(line) < 7:
                wordList.append(line[0:-1])
    return wordList

def printArt(art):
    for line in art:
        print(line)

def setParts():
    parts = {
        1 : head,
        2 : body,
        3 : leftArm,
        4 : rightArm,
        5 : leftLeg,
        6 : rightLeg,
        }
    return parts

def head(art):
    art.insert(2, '       +---+       |');
    art.insert(2, '       +0 0+       |');
    art.insert(2, '       +---+       |');

def body(art):
    art.insert(5, '      +-----+      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +-----+      |');
    art.insert(5, '         +         |');

def leftArm(art):
    art[6] = '    --+-----+      |';
    art[7] = '   +  +     +      |';
    art[8] = '   +  +     +      |';
    art[9] = '  +   +     +      |';

def rightArm(art):
    art[6] = '    --+-----+--    |';
    art[7] = '   +  +     +  +   |';
    art[8] = '   +  +     +  +   |';
    art[9] = '  +   +     +   +  |';

def leftLeg(art):
    art[11] = '       +           |';
    art[12] = '      +            |';
    art[13] = '      +            |';
    art[14] = '     +             |';

def rightLeg(art):
    art[11] = '       +   +       |';
    art[12] = '      +     +      |';
    art[13] = '      +     +      |';
    art[14] = '     +       +     |';

def init():
    bodyParts = setParts()
    art = makeArt()
    words = readWords()
    return bodyParts, art, words

def insertletter (spaces, letter, pos):
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos+1:]
    return spaces

count = 0
count2 = 0
#word = random.choice(readWords())
word = 'neno'
print(word)
spaces = '_ ' * len(word)
bodyParts, art, words = init()
printArt(art)
for i in range(6):
    guess = input('letter? ')
    for i in range(len(word)):
        if guess == word[i]:
            pos = word.index(guess)
            print(word[i])
            #word[i] = '.'
            count2 = count2 + 1
            spaces = insertletter(spaces, guess, pos)
    #print(count2)
    if guess not in word:
        count = count + 1
        misses = count
        bodyParts[misses](art)
        printArt(art)
    #print(count)
    print(spaces)
