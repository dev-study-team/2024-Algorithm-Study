
7662문제와 비슷하다 동기화를 해주면 쉬운문제이다.

import sys, heapq

N = int(sys.stdin.readline())

max_heap = []
min_heap = []
d = [0] * 100001
for i in range(N) :
    p, l = map(int, sys.stdin.readline().split())
    heapq.heappush(max_heap, (-l, -p))
    heapq.heappush(min_heap, (l, p))
    d[p] = 1

M = int(sys.stdin.readline())
result = []
for i in range(M) :
    command = sys.stdin.readline().split()
    if "add" == command[0] :
        # add 되려면 똑같은 문제가 추천 리스트에 없어야함 즉 이미 풀린 문제이거나 그래야하는거 그래서 pop을해서 다 내보내는거
        while max_heap and d[-max_heap[0][1]] == 0 : # 사용한것들은 다 삭제 
            heapq.heappop(max_heap)
        while min_heap and d[min_heap[0][1]] == 0 : # 사용한 것들 다 삭제 
            heapq.heappop(min_heap)
        p, l = int(command[1]), int(command[2])

        heapq.heappush(min_heap,(l ,p)) # 레벨 ,문제 번호
        heapq.heappush(max_heap,(-l ,-p))
        d[p] = 1
    elif "recommend" == command[0] :
        if command[1] == "1" :
            while max_heap and d[-max_heap[0][1]] == 0 :
                heapq.heappop(max_heap)
            result.append(-max_heap[0][1])
        else : 
            while min_heap and d[min_heap[0][1]] == 0 :
                heapq.heappop(min_heap)
            result.append(min_heap[0][1])
    elif "solved" == command[0] :
        d[int(command[1])] = 0

print('\n'.join(map(str, result)))
