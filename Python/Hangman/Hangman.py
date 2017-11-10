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
    
    misses = 1
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

'''
s = 'apple'
letters = list(s)
print(letters)

letters = ','.join(letters)
print(letters)

w = 'cat dog fish'
w = w.split(' ')
print(w)
'''

pic = [1,2,3,4]
pic[0] = '============='
pic[1] = '=           ='
pic[2] = '=           ='
pic[3] = '============='

#foo = [5,6,7,8,9,0]

def printPic(p): #Assumes p is a list
    for line in p:
        print(line)

printPic(pic)
pic[2] = '=***********='
printPic(pic)
#printPic(foo)


def insertletter (spaces, letter, pos):
    #_ _ _ _ ...
    #0123456 ...
    #pos * 2 is the location in spaces
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos+1:]
    return spaces



word = 'donut'
spaces = '_ ' * len(word)

for i in range(len(word)):
    guess = input('letter? ')
    if guess in word:
        pos = word.index(guess)
        spaces = insertletter(spaces, guess, pos)
    else:
        print('nope')

    #pic[4] = spaces
    #printPic(pic)
    
    print(spaces)
    
"""
spaces = '_ ' * len(word)
print(spaces)

spaces = insertletter(spaces, 'o', 1)
print(spaces)

spaces = insertletter(spaces, 't', 4)
print(spaces)

letters = list(word)
print(letters)
"""





