
def move1meter(distance, direction): #distance in intergers of meters - direction L or R
        left = 0
        right = 0
        count = 0
        addleft = 0
        addright = 0
        if direction == 'L':
            while addleft < distance:
                addleft = count + 1
                addleft = addleft + addleft
                left = left + addleft
                addright = count + 1
                addright = addright + addright
                right = right + addright
                count = count + 1
        if direction == 'R':
            while addright < distance:
                addleft = count + 1
                addleft = addleft + addleft
                left = left + addleft
                addright = count + 1
                addright = addright + addright
                right = right + addright
                count = count + 1
        return left + right

print(move1meter(50, 'R'))


