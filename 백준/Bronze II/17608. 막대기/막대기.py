import sys

input = sys.stdin.readline
numbers = int(input())
stack = []

for x in range(numbers):
    stack.append(int(input()))

last = stack[-1]
count = 1

for i in reversed(range(numbers)):
    if stack[i]>last:
        count+=1
        last=stack[i]
print(count)