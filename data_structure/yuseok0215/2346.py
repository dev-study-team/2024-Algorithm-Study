"""
어느정도 접근을 했지만 최종결과를 만들지 못한 문제..

enumerate를 사용해서 해결하는 것이 주요했다.

enumerate 사용 전
deque([3, 2, 1, -3, -1])
enumerate 사용 후
deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

rotate 이해가 안가네요..

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))

"""

import sys

n = int(sys.stdin.readline())
data = list(enumerate((map(int, sys.stdin.readline().split())), start = 1)) # (인덱스, 값) 구조로 저장
idx = 0 # 첫번째 idx 고정

while data: # data가 존재하는 동안
	ret = data.pop(idx) # 추출 값
	print(ret[0], end=' ') # 인덱스 출력
	if ret[1] < 0 and data: # 다음 인덱스 위치가 음수면
		idx = (idx + ret[1]) % len(data) # 왼쪽으로
	elif ret[1] > 0 and data: # 다음 인덱스 위치가 양수면
		idx = (idx + (ret[1] - 1)) % len(data) # pop한 1덱스 하나 제외 후 오른쪽으로


# 내 틀린 풀이

# n = int(input())
# bal = list(map(int, input().split()))

# bal_idx = [i for i in range(1,n+1)] 

# pop_idx = 0
# move_idx = bal[0] # 초기 설정

# ans = []

# while True:
#     bal.pop(pop_idx)
#     ans.append(bal_idx.pop(pop_idx))

#     if len(bal) == 0:
#         break

#     if pop_idx + move_idx >=0:
#         pop_idx = (pop_idx + move_idx) % len(bal) 
#     else:
#         pop_idx = len(bal) - ((-(pop_idx + move_idx)) % len(bal))

#     pop_idx -= 1
#     move_idx = bal[pop_idx]

# for elem in ans:
#     print(elem, end='')

    
    











# ans = [] # 터진 풍선 순서
# current_idx = 0
# target_idx = 0 # 터질 풍선 idx

# while True:
#     if len(bal) == 1:
#         ans.append(bal_idx[0])
#         break

#     current_length = len(bal)
#     move_idx = bal[target_idx] # 이동 인덱스
#     bal.pop(target_idx) # 풍선 터짐
#     ans.append(bal_idx.pop(target_idx)) # 터진 순서에 추가

#     if current_idx + move_idx < 0:
#         target_idx = len(bal) + move_idx 
#     else:
#         target_idx = (target_idx + move_idx-1) % len(bal)
    
    
#     current_idx = target_idx

# print(ans)