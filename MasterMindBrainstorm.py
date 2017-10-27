

# Four colors: Red, Green, Blue, White
# Put colored pegs in four holes
#   No empty holes
#   Can repeat colors (RRRR for example)
# 
# A code is created as above
# And the user repeatedly gueses the code
#   RRGG, RGBW, WWWW, ....
# Feedback: (Tricky)
#   Code: RGBW
#   User: RRWB --> CBB                      (C is a match on color & position)
#         RRWW --> CB (no) should be CC     (B is a match on color only)
# (second R doesn't get anything because the R has already been revealed)
#
#   Code: RRGG
#   User: BRRG --> CBC
#       
#   No implied position (Don't know which one is right color right place)
#   white peg for right color right location
#   black peg for right color wrong location
#   nothing for no matches
#   User can keep going in this example game
#
# Tasks:
#   --How are the code and guess represented in the code?
#       --((characters)), String, array, letters, class
#   --Create a random code (easy)
#   --Get the user's guess (easy)
#       Optional: check for valid guess (all letters etc.) (medium)
#   --Compare user guess to code (medium)
#       --1. look for exact matches (medium)
#       --2. Change matches to X (medium)
#       --3. look for remaining matches (medium)
#       --4. Change matches to X (medium)
#   --Report result (easy)
#       --Optional: Repeat until guessed (easy)

#Generate Rondom Code
ClrOptions = ['R','G','B','W']
import random
Clr1 = random.choice(ClrOptions)
Clr2 = random.choice(ClrOptions)
Clr3 = random.choice(ClrOptions)
Clr4 = random.choice(ClrOptions)
Code = [Clr1, Clr2, Clr3, Clr4]
CodeRestore = list(Code)
#print(CodeRestore)
print(Code)

Result = 'B'
while Result != ['C','C','C','C']:
    CodeRestore = list(Code)
    #Get User Guess
    myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
    myGuess = myGuess.upper()
    myGuess = list(myGuess)
    #print(myGuess)

    # Check for valid entry
    #if len(myGuess) != len(Code):
        #print('Oops, not a valid entry. This entry is either too short or too long. 4 digits please.')
    while len(myGuess) != len(Code):
        if len(myGuess) != len(Code):
            print('Oops, not a valid entry. This entry is either too short or too long. 4 digits please.')
        #print('Oops, not a valid entry. This entry is either too short or too long. 4 digits please.')
        myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
        myGuess = myGuess.upper()
        myGuess = list(myGuess)

    while myGuess[0] not in ClrOptions or myGuess[1] not in ClrOptions or myGuess[2] not in ClrOptions or myGuess[3] not in ClrOptions:
        if myGuess[0] not in ClrOptions or myGuess[1] not in ClrOptions or myGuess[2] not in ClrOptions or myGuess[3] not in ClrOptions:
            print('Oops, not a valid entry. Please only use the letters R, G, B, W.')
        #print('Oops, not a valid entry. This entry is either too short or too long. 4 digits please.')
        myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
        myGuess = myGuess.upper()
        myGuess = list(myGuess)

    # Compare - Look for exact matches
    count = 0
    for i in range(4):
        if Code[i] == myGuess[i]:
            count = count + 1
            Code[i] = 'X'
            myGuess[i] = 'Z'
    #print(Code)
    #print(myGuess)
    #print(count)
    Result = 'C' * count
    #print(Result)

    # Compare - Look for semi-matches
    count = 0
    for i in range(4):
        if Code[i] in myGuess[0]:
            count = count + 1
            Code[i] = 'X'
            myGuess[0] = 'Z'
        if Code[i] in myGuess[1]:
            count = count + 1
            Code[i] = 'X'
            myGuess[1] = 'Z'
        if Code[i] in myGuess[2]:
            count = count + 1
            Code[i] = 'X'
            myGuess[2] = 'Z'
        if Code[i] in myGuess[3]:
            count = count + 1
            Code[i] = 'X'
            myGuess[3] = 'Z'
    #print(Code)
    #print(myGuess)
    #print(count)
    Result = Result + 'B' * count
    #print(Result)
    Result = list(Result)

    # Report Result
    def scrambled(orig):
        dest = orig[:]
        random.shuffle(dest)
        return dest
    Result = scrambled(Result)
    #Result = str(Result[0]+Result[1]+Result[2]+Result[3])
    print(Result)
    #print(CodeRestore)
    Code = CodeRestore
    #print(Code)
    if Result == ['C','C','C','C']:
        print('YOU WON!')


def okCharacters(chars):
    validLetters = ['A','Z','T','C']
    charsOK = (len(chars) > 0 )

    for ch in chars:
        if ch not in validLetters:
            charsOK = False

    return charsOK

def compareLists(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            pass #exact match
        
letters = ['B']

if okCharacters(letters):
    print('good input')
else:
    print('bad input')
