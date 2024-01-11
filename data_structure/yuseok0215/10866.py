from collections import deque

n = int(input())

command = []
for i in range(n):
    command.append(input())


q = deque()
for elem in command:
    operation = elem.split()

    if operation[0] == 'push_front':
        q.appendleft(operation[1])
    elif operation[0] == 'push_back':
        q.append(operation[1])
    elif operation[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif operation[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())    
    elif operation[0] == 'size':
        print(len(q))
    elif operation[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif operation[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif operation[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])   