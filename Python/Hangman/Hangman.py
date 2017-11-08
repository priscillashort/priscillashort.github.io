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
    art.append('         +---------+') #0
    art.append('         |         |') #1
    art.append('                   |') #etc
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
    for line in art: #line is a var
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

def main():
    bodyParts, art, words = init()
    
    printArt(art)
    
    if misses = 1:
    bodyParts[misses](art)
    
    misses = 2
    bodyParts[misses](art)

    misses = 3
    bodyParts[misses](art)

    misses = 4
    bodyParts[misses](art)

    misses = 5
    bodyParts[misses](art)

    misses = 6
    bodyParts[misses](art)
    
    printArt(art);
    
    for i in range(20):
        print(random.choice(words))

main()
