def solution(numbers, hand):

    keypad = {  1:(0,1), 2:(0,2), 3:(0,3),
                4:(1,1), 5:(1,2), 6:(1,3),
                7:(2,1), 8:(2,2), 9:(2,3),
              '*':(3,1), 0:(3,2), '#':(3,3) }
    
    l_pos=keypad['*']
    r_pos=keypad['#']
    
    result=''
    
    for num in numbers:
        if num in [1,4,7]:
            result+='L'
            l_pos=keypad[num]
        elif num in [3,6,9]:
            result+='R'
            r_pos=keypad[num]
        else:
            l_distance= abs(keypad[num][0]-l_pos[0]) + abs(keypad[num][1]-l_pos[1])
            r_distance= abs(keypad[num][0]-r_pos[0]) + abs(keypad[num][1]-r_pos[1])
            if l_distance<r_distance:
                result+='L'
                l_pos=keypad[num]
            elif l_distance>r_distance:
                result+='R'
                r_pos=keypad[num]
            elif l_distance==r_distance:
                if hand=='left':
                    result+='L'
                    l_pos=keypad[num]
                else:
                    result+='R'
                    r_pos=keypad[num]

    return result