# https://www.acmicpc.net/problem/18258

# 10828 문제와 다를 것이 없으며 아래와 같이 deque를 쓰지 않고 list를 이용해 풀 수 있다.


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
            print(deque.popleft())
    elif "size" in findStr :
        print(len(deque))
    elif "empty" in findStr :
        if len(deque) == 0 :
            print(1)
        else :
            print(0)
    elif "front" in findStr :
        if len(deque) == 0 :
            print(-1)
        else :
            num = deque.popleft()
            print(num)
            deque.appendleft(num)    
    elif "back" in findStr :
        if len(deque) == 0 :
            print(-1)
        else :
            num = deque.pop()
            print(num)
            deque.append(num) 




