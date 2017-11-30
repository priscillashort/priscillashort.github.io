# Conway's Game of Life
# Written by Priscilla Short on 11-22-17
print('Please input 5 x and y coordinates to points on a graph to start the game:')
populatedCells = []
for i in range(5):
    x = int(input('x: '))
    y = int(input('y: '))
    cell = [x, y]
    populatedCells.append(cell)
print('Originally popuplated cells:', populatedCells)
play = input("Enter the word 'STEP' to trigger the rules and cause the points to change: ")
play = play.upper()
while play == 'STEP':
    remove = []
    emptyCells = []
    for j in range(len(populatedCells)):
        count = 0
        origCell = [populatedCells[j][0], populatedCells[j][1]]
        cella = [populatedCells[j][0] - 1, populatedCells[j][1] + 1]
        cellb = [populatedCells[j][0], populatedCells[j][1] + 1]
        cellc = [populatedCells[j][0] + 1, populatedCells[j][1] + 1]
        celld = [populatedCells[j][0] - 1, populatedCells[j][1]]
        celle = [populatedCells[j][0] + 1, populatedCells[j][1]]
        cellf = [populatedCells[j][0] - 1, populatedCells[j][1] - 1]
        cellg = [populatedCells[j][0], populatedCells[j][1] - 1]
        cellh = [populatedCells[j][0] + 1, populatedCells[j][1] - 1]
        if cella in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cella)
            
        if cellb in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellb)
            
        if cellc in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellc)
            
        if celld in populatedCells:
            count = count + 1
        else:
            emptyCells.append(celld)
            
        if celle in populatedCells:
            count = count + 1
        else:
            emptyCells.append(celle)
            
        if cellf in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellf)
            
        if cellg in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellg)
            
        if cellh in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellh)
            
        if count == 1 or count == 0:
            remove.append(origCell)
        if count >= 4:
            remove.append(origCell)

    AddedCells = []
    for l in range(len(emptyCells)):
        count = 0
        origCell = [emptyCells[l][0], emptyCells[l][1]]
        cella = [emptyCells[l][0] - 1, emptyCells[l][1] + 1]
        cellb = [emptyCells[l][0], emptyCells[l][1] + 1]
        cellc = [emptyCells[l][0] + 1, emptyCells[l][1] + 1]
        celld = [emptyCells[l][0] - 1, emptyCells[l][1]]
        celle = [emptyCells[l][0] + 1, emptyCells[l][1]]
        cellf = [emptyCells[l][0] - 1, emptyCells[l][1] - 1]
        cellg = [emptyCells[l][0], emptyCells[l][1] - 1]
        cellh = [emptyCells[l][0] + 1, emptyCells[l][1] - 1]
        if cella in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cella)
            
        if cellb in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellb)
            
        if cellc in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellc)
            
        if celld in populatedCells:
            count = count + 1
        else:
            emptyCells.append(celld)
            
        if celle in populatedCells:
            count = count + 1
        else:
            emptyCells.append(celle)
            
        if cellf in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellf)
            
        if cellg in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellg)
            
        if cellh in populatedCells:
            count = count + 1
        else:
            emptyCells.append(cellh)
            
        if count == 3:
            if origCell not in AddedCells:
                AddedCells.append(origCell)

    populatedCellsCopy = []
    for k in range(len(populatedCells)):
        if populatedCells[k] not in remove:
            populatedCellsCopy.append(populatedCells[k])
    populatedCells = list(populatedCellsCopy)
    for m in range(len(AddedCells)):
        populatedCells.append(AddedCells[m])

    print('Cells curently populated:', populatedCells)
    play = input("Enter the word 'STEP' to trigger the rules and cause the points to change: ")
    play = play.upper()
