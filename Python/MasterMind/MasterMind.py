#Generate Rondom Code
ClrOptions = ['R','G','B','W']
import random
Clr1 = random.choice(ClrOptions)
Clr2 = random.choice(ClrOptions)
Clr3 = random.choice(ClrOptions)
Clr4 = random.choice(ClrOptions)
Code = [Clr1, Clr2, Clr3, Clr4]
CodeRestore = list(Code)

# Initialize
print('Welcome to the Master Mind game! Try using invalid entries to test the error handling')
Result = 'place holder'
NumTries = 0
while Result != 'CCCC':
    CodeRestore = list(Code)
    
    #Get User Guess
    myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
    myGuess = myGuess.upper()
    myGuess = list(myGuess)

    # Check for valid entry
    while len(myGuess) != len(Code) or myGuess[0] not in ClrOptions or myGuess[1] not in ClrOptions or myGuess[2] not in ClrOptions or myGuess[3] not in ClrOptions:
        while len(myGuess) != len(Code):
            if len(myGuess) != len(Code):
                print('Oops, not a valid entry. This entry is either too short or too long. 4 digits please.')
            myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
            myGuess = myGuess.upper()
            myGuess = list(myGuess)
        while myGuess[0] not in ClrOptions or myGuess[1] not in ClrOptions or myGuess[2] not in ClrOptions or myGuess[3] not in ClrOptions:
            if myGuess[0] not in ClrOptions or myGuess[1] not in ClrOptions or myGuess[2] not in ClrOptions or myGuess[3] not in ClrOptions:
                print('Oops, not a valid entry. Please only use the letters R, G, B, W.')
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
    Result = 'C' * count

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
    Result = Result + 'B' * count
    Result = list(Result)

    # Report Result
    def scrambled(orig):
        dest = orig[:]
        random.shuffle(dest)
        return dest
    Result = scrambled(Result)
    Result = ''.join(Result)
    print(Result)
    Code = CodeRestore
    NumTries = NumTries + 1
    if Result == 'CCCC':
        print('YOU WON! It took you',NumTries,'tries to guess the code.')
        input('Enter any key to exit: ')

