def solution(numbers):
    answer = ''
    # numbers=str(numbers)
    for idx,i in enumerate(numbers):
        numbers[idx]=str(i)
    numbers.sort(key = lambda x : x*3,reverse=True)
    # print(numbers)
    return (str(int(('').join(numbers))))