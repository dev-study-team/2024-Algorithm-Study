# https://www.acmicpc.net/problem/10828


"""
내생각
그냥 deque에 넣으면 된다 생각이 들어 구현에 들어가게 되었다.

어려웠던점, 이슈
input으로 하는게 시간이 오래걸려서 count = int(sys.stdin.readline())로 구현해야했는데 몰라서 어려웠었다


"""

from collections import deque
import sys
count = int(sys.stdin.readline())

deque = deque()
for i in range(count) :
    findStr = sys.stdin.readline()
    if "push" in findStr :
        num = findStr.split()
        deque.append(int(num[1]))
    elif "pop" in findStr :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque.pop())
    elif "size" in findStr :
        print(len(deque))
    elif "empty" in findStr :
        if len(deque) == 0 :
            print(1)
        else :
            print(0)
    elif "top" in findStr :
        if len(deque) == 0 :
            print(-1)
        else :
            num = deque.pop()
            print(num)
            deque.append(num)    

"""
https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EC%8A%A4%ED%83%9D10828%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%8A%A4%ED%83%9D

deque를 이용해 풀지 않고 list를 이용해 풀 수 있다.

import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

"""








