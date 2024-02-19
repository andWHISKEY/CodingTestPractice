def solution(numbers, hand):
    result = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    left_loc=dic['*']
    right_loc=dic['#']
    
    for i in numbers:
        if i in [1,4,7]:
            result+='L'
            left_loc=dic[i]
        elif i in [3,6,9]:
            result+='R'
            right_loc=dic[i]
        #2,5,8,0
        else:
            left_dis=0
            right_dis=0
            
            #얼마나 가까운지 어떻게 계산하지? 
            for a,b,c in zip(left_loc,right_loc,dic[i]):
                left_dis+=abs(a-c)
                right_dis+=abs(b-c)
            
            if left_dis<right_dis:
                result+='L'
                left_loc=dic[i]
            elif left_dis>right_dis:
                result+='R'
                right_loc=dic[i]
            else:
                if hand=='left':
                    result+='L'
                    left_loc=dic[i]
                else:
                    result+='R'
                    right_loc=dic[i]
    
    return result