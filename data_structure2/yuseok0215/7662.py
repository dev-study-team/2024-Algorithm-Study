"""
heapq와 visited의 조합으로 푸는 문제 

나는 visited 대신 새로운 배열을 가져와서 시간초과가 났다..
"""

import heapq

t = int(input())

for _ in range(t):
    k = int(input()) # Q에 적용할 연산의 개수

    visit = [False] * 1_000_001

    heap_min = []
    heap_max = []
    heap = []
    for _ in range(k):
        oper, n = input().rstrip().split()
        n = int(n)

        #  -5746 16 min
        # -16 5746 max

        if oper == 'I':
            heapq.heappush(heap_min, n)
            heapq.heappush(heap_max, -n)
            visit[n] = True # 힙에서 아직 삭제 되지 않은 상태
        
        elif oper == 'D' and n == 1:
            if len(heap_max) >= 1:
                res = -heapq.heappop(heap_max)
                heap_min.remove(res)
                visit[res] = False
            
        elif oper == 'D' and n == -1:
            if len(heap_min) >= 1:
                res = heapq.heappop(heap_min)
                heap_max.remove(-res)
                visit[res] = False

    if len(heap) == 0:
        print('EMPTY')
    else:
        print(str(max(heap)) + ' ' + str(min(heap)))
    
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
        