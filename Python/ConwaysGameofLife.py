populatedCells = []
for i in range(5):
    x = int(input('x: '))
    y = int(input('y: '))
    populatedCells.append(x)
    populatedCells.append(y)

print(populatedCells)
    
for j in range(len(populatedCells) // 2):
    cella = [int(x)+1,int(y)]

print(cella)
