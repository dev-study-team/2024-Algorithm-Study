"""
- 접근방법

"""
from collections import deque

n = int(input())

cards = [i for i in range(1,n+1)]

queue = deque(cards)

while True:
    if len(queue) == 1:
        print(queue[0])
        break
        
    queue.popleft()
    move_num = queue.popleft()
    queue.append(move_num)

