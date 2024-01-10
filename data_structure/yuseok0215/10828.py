import sys
input = sys.stdin.readline

N = int(input())

operation = []

for i in range(N):
    operation.append(input())

stack_list = []

for op in operation:
    op_split = op.split()

    if(op_split[0] == 'push'):
        stack_list.append(op_split[1])
    
    elif(op_split[0] == 'pop'):
        if(len(stack_list) == 0):
            print(-1)
        elif(len(stack_list) != 0):
            print(stack_list[-1])
            stack_list.pop()
    
    elif(op_split[0] == 'size'):
        print(len(stack_list))
    
    elif(op_split[0] == 'empty'):
        if(len(stack_list) == 0):
            print(1)
        elif(len(stack_list) != 0):
            print(0)

    elif(op_split[0] == 'top'):
        if(len(stack_list) == 0):
            print(-1)
        elif(len(stack_list) != 0):
            print(stack_list[-1])

"""
1. 접근 방법
조건별로 꼼꼼하게 구현하면 문제 없겠다!

2. 문제의 핵심 알고리즘
...?

3. 시간 복잡도 
O(n)
"""