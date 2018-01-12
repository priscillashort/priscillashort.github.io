#Hangman game: completed by Priscilla Short on 11.10.17

#Functions:
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
        7 : leftFoot,
        8 : rightFoot,
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


def leftFoot(art):
    art[11] = '       +   +       |';
    art[12] = '      +     +      |';
    art[13] = '      +     +      |';
    art[14] = '   --+       +     |';

def rightFoot(art):
    art[11] = '       +   +       |';
    art[12] = '      +     +      |';
    art[13] = '      +     +      |';
    art[14] = '   --+       +--   |';

def init():
    bodyParts = setParts()
    art = makeArt()
    words = readWords()
    return bodyParts, art, words

def insertletter (spaces, letter, pos):
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos+1:]
    return spaces

#Play again loop
print('Welcome to the Hangman game! Try using invalid entries to test the error handling. You have 8 misses and then you are dead.')
play = 'YES'
while play == 'YES': 
    #Initialisation:
    print()
    print()
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    guessed = []
    count = 0
    word = random.choice(readWords())
    word = word.upper()
    word = list(word)
    saveWord = list(word)
    saveWord = ''.join(saveWord)
    spaces = '_ ' * len(word)
    bodyParts, art, words = init()
    printArt(art)
    print(spaces)
    print()
    win = '?' * len(word)
    win = list(win)
    misses = 0
    #Main game loop
    while word != win and misses != 8:
        guess = input('Enter a letter: ').upper()
        print()
        #Test for valid input
        while guess not in alphabet or guess in guessed:
            while guess not in alphabet:
                print('Oops, that is not a letter.')
                guess = input('Enter a letter: ').upper()
                print()
            while guess in guessed:
                print('Oops, you have already guessed that letter.')
                guess = input('Enter a letter: ').upper()
                print()
        #Check if the letter is NOT in the word
        if guess not in word:
            count = count + 1
            misses = count
            bodyParts[misses](art)
            printArt(art)
        #Check if the letter is in the word and what position
        for i in range(len(word)):
            if word[i] == guess:
                pos = word.index(guess)
                spaces = insertletter(spaces, guess, pos)
                word[i] = '?'
        #modify letters guessed list and display outputs
        guessed.append(guess)
        print('Letters already guessed: ', guessed)
        print(spaces)
        print()
        #Check if the user won
        if word == win:
            print('You won!')
            play = input("Would you like to play again? Type 'yes' to play and any other key to exit: ").upper()
        #Check if the user lost
        if misses == 8:
            print('You lost.')
            print('The word was: ', saveWord)
            play = input("Would you like to play again? Type 'yes' to play and any other key to exit: ").upper()
            

