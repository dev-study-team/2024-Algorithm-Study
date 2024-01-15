import sys

input = sys.stdin.readline

arr = input()

result = 0
stack = []
for i in range(len(arr)):
    # ( ) [ ]
    if arr[i] == '(':
        stack.append('(')
    elif arr[i] == '[':
        stack.append('[')
    elif arr[i] == ')':
        if arr[i-1] == '(':
            result += 2
        elif arr[i-1] == ')' or arr[i-1] == ']':
            result *= 2
        else:
            print(0)
            break
    elif arr[i] == ']':
        if arr[i-1] == '[':
            result += 3
        elif arr[i-1] == ')' or arr[i-1] == ']':
            result *= 3
        else:
            print(0)
            break

print(result)
         

