def solution(sizes):
    for i in sizes:
        if i[0]>i[1]:
            i[0],i[1]=i[1],i[0]
    x_max=max(list(zip(*sizes))[0])
    y_max=max(list(zip(*sizes))[1])
    answer = x_max*y_max
    return answer