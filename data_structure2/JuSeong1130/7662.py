
pypy3로 통고한문제인데 아래 isEmpty를 없애고 구현하면 시간초과가 나지 않는다
또한 문제에서 중점인게 있었는데 동기화였다.
visited라는 배열을 통해 이미 방문하였다면 pop해주는 방식을 통해 진행하였다.
단 가중치를 중점으로 두는게 아니라 이렇게했을때 통과했지만 가중치를 한다면 이차원 배열로 구현하여 방문하였는지 확인해야한다. 

import heapq,sys


def isEmpty(nums) :
    for num in nums.items() :
        if num[1] > 0 :
            return False
    return True


T = int(sys.stdin.readline())
for _ in range(T) :
    K = int(sys.stdin.readline())
    max_heapq = []
    min_heapq = []
    d = dict()
    for i in range(K) :
        left, right = sys.stdin.readline().split()
        right = int(right)

        if left == "I" :
            if right in d :
                d[right] = d[right] + 1
            else :
                d[right] = 1
                heapq.heappush(max_heapq, -right)
                heapq.heappush(min_heapq, right)
            
        else :
            if isEmpty(d) : # 큐가 비어있으면 삭제 불가
                continue
            if right == 1 : # 최대값 삭제
               while -max_heapq[0] not in d or d[-max_heapq[0]] < 1 : # 허수들 삭제 하고 진짜 max 값 찾기
                    temp = -heapq.heappop(max_heapq)
                    if temp in d :
                        del d[temp]
               d[-max_heapq[0]] -= 1 # 진짜 max값 사용했다는 의미로 -1
            else : # 허수들 삭제 하고 진짜 min 값 찾기
               while min_heapq[0] not in d or d[min_heapq[0]] < 1 :
                   temp = heapq.heappop(min_heapq)
                   if temp in d :
                       del d[temp]
               d[min_heapq[0]] -= 1
    if isEmpty(d) :
        print("EMPTY")
    else :
        while -max_heapq[0] not in d or d[-max_heapq[0]] < 1 : # 허수들 삭제 하고 진짜 max 값 찾기
                    temp = -heapq.heappop(max_heapq)
        while min_heapq[0] not in d or d[min_heapq[0]] < 1 :
                   temp = heapq.heappop(min_heapq)
        print(-heapq.heappop(max_heapq),heapq.heappop(min_heapq))


아래와 같이 하면된다.

# import sys
# import heapq
# input = sys.stdin.readline


# test = int(input())
# for _ in range(test):
#     max_heap, min_heap = [], []
#     visit = [False] * 1_000_001

#     order_num = int(input())

#     for key in range(order_num):
#         order = input().rsplit()
#         if order[0] == 'I':
#             heapq.heappush(min_heap, (int(order[1]), key))
#             heapq.heappush(max_heap, (int(order[1]) * -1, key))
#             visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

#         elif order[0] == 'D':
#             if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
#                 # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
#                 while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
#                     heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
#                 if min_heap:
#                     visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
#                     heapq.heappop(min_heap)
#             elif order[1] == '1':
#                 while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
#                     heapq.heappop(max_heap)
#                 if max_heap:
#                     visit[max_heap[0][1]] = False
#                     heapq.heappop(max_heap)

# # 모든 연산이 끝난후에도 ㅅ쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
#     while min_heap and not visit[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#     while max_heap and not visit[max_heap[0][1]]:
#         heapq.heappop(max_heap)

#     if min_heap and max_heap:
#         print(-max_heap[0][0], min_heap[0][0])
#     else:
#         print('EMPTY')

  
