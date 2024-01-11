from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    doc = list(map(int, input().split()))
    
    if len(doc) == 1:
        print(1)
        continue

    q = deque(doc)

    initial_idx = [i for i in range(n)]
    idx_q = deque(initial_idx)

    cnt = 0
    while True:
        if len(q) == 1:
            print(cnt+1)
            break

        num = q.popleft()
        num_idx = idx_q.popleft()

        if num < max(q):
            q.append(num)
            idx_q.append(num_idx)
        else:
            cnt += 1
            if num_idx == m:
                print(cnt)
                break        
