play = 'YES'
while play == 'YES':
    #Computer's choice
    myList = ['ROCK', 'PAPER', 'SCISSORS']
    import random
    compChoice = random.choice(myList)
    #My choice
    myChoice = input('Please choose rock, paper, or scissors: ')
    myChoice = myChoice.upper()
    if myChoice not in myList:
        print('Oops, not a valid entry.')
    while myChoice not in myList:
        myChoice = input('Please choose rock, paper, or scissors: ')
        myChoice = myChoice.upper()
        if myChoice not in myList:
            print('Oops, not a valid entry.')
    #Test for tie
    if compChoice == myChoice:
        print("It's a tie.")
    #Test if I won
    if (myChoice == 'ROCK' and compChoice == 'SCISSORS') or (myChoice == 'PAPER' and compChoice == 'ROCK') or (myChoice == 'SCISSORS' and compChoice == 'PAPER'):
        print('You won!')
    #Test if computer won      
    if (myChoice == 'ROCK' and compChoice == 'PAPER') or (myChoice == 'PAPER' and compChoice == 'SCISSORS') or (myChoice == 'SCISSORS' and compChoice == 'ROCK'):
        print('You lost. Bummer.') 
    #Play again?
    play = input("Would you like to play again? Type 'yes' to play and any other key to exit: ")
    play = play.upper()
