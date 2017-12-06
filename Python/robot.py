
def move1meter(distance, direction): #distance in intergers of meters - direction L or R
        left = 0
        right = 0
        count = 0
        addleft = 0
        addright = 0
        if direction == 'L':
            while (addleft / 2) < distance:
                addleft = count + 1
                if addleft >= distance:
                        left = left + addleft
                        break
                addleft = addleft + addleft
                left = left + addleft
                addright = count + 1
                addright = addright + addright
                right = right + addright
                count = count + 1
                
        if direction == 'R':
            while (addright / 2) < distance:
                addleft = count + 1
                addleft = addleft + addleft
                left = left + addleft
                addright = count + 1
                if addright >= distance:
                        right = right + addright
                        break
                addright = addright + addright
                right = right + addright
                count = count + 1
        return left + right

def movexand1meter(distance, direction): #distance in intergers of meters - direction L or R
        left = 0
        right = 0
        count = 0
        addleft = 0
        addright = 0
        add = 1
        if direction == 'L':
            while (addleft / 2) < distance:
                addleft = count + add
                if addleft >= distance:
                        left = left + addleft
                        break
                addleft = addleft + addleft
                left = left + addleft
                add = add + 1
                addright = count + 1
                addright = addright + addright
                right = right + addright
                count = count + 1
                add = add + 1
                
        if direction == 'R':
            while (addright / 2) < distance:
                addleft = count + 1
                addleft = addleft + addleft
                left = left + addleft
                add = add + 1
                addright = count + 1
                if addright >= distance:
                        right = right + addright
                        break
                addright = addright + addright
                right = right + addright
                count = count + 1
                add = add + 1
        return left + right

print(movexand1meter(10, 'L'))


