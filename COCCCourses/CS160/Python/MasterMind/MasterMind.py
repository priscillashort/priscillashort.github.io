print('Welcome to the Master Mind game! Try using invalid entries to test the error handling')
print('Please note that C means an exact match in the exact location and B means a match but not in the correct spot.')
play = 'YES'
while play == 'YES':
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
    Result = 'place holder'
    NumTries = 0
    while Result != 'CCCC':
        CodeRestore = list(Code)
        
        #Get User Guess
        myGuess = input('Please choose a 4 digit combination of R(Red), G(Green), B(Blue), and W(White): ')
        myGuess = myGuess.upper()
        myGuess = list(myGuess)
        
        # Check for valid entry
        def ValidEntry(a, b, c): #a=len(myGuess) b=myGuess c=ClrOptions 
            counter1 = 0
            for i in range(a):
                if b[i] not in c:
                    counter1 = counter1 + 1
            if a != 4:
                counter1 = counter1 + 1
            if counter1 > 0:
                return False
        while ValidEntry(len(myGuess), myGuess, ClrOptions) == False:
            print('Oops, not a valid entry. This entry is either the wrong length or uses invalid letters.')
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
            play = input("Would you like to play again? Type 'yes' to play and any other key to exit: ")
            play = play.upper()


