n = int(input())

operation = []

for i in range(n):
    operation.append(input())

queue = []
for elem in operation:
    oper = elem.split()

    if oper[0] == 'push':
        queue.append(oper[1])

    elif oper[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    
    elif oper[0] == 'size':
        print(len(queue))
    
    elif oper[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif oper[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif oper[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])        
           

