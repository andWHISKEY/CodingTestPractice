def solution(array, commands):
    answer = []
    for i,j,k in commands:
        # print(sorted(array[i-1:j])[k-1])
        answer.append(sorted(array[i-1:j])[k-1])
    return answer