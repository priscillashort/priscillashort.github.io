

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
#   How are the code and guess represented in the code?
#       ((characters)), String, array, letters, class
#   Create a random code (easy)
#   Get the user's guess (easy)
#       Optional: check for valid guess (all letters etc.) (medium)
#   Compare user guess to code (medium)
#       1. look for exact matches (medium)
#       2. Change matches to X (medium)
#       3. look for remaining matches (medium)
#       4. Change matches to X (medium)
#   Report result (easy)
#       Optional: Repeat until guessed (easy)

x = ['R','R','G','B']
y = ['R','G','R','B']
count = 0
for i in range(4):
    if x[i] == y[i]:
        count = count + 1
        x[i] = 'Z'
        y[i] = 'H'
print(x)
print(y)
print(count)
