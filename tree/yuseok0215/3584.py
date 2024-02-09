t = int(input())

for _ in range(t):
    n = int(input())

    parent = [0] * (n+1)
    for _ in range(n-1):
        a,b = map(int, input().split())
        parent[b] = a

    a,b = map(int, input().split())

    a_parent = [a] # 같은 라인에서 서로 부모 자식 관계일 수 있기 때문에
    b_parent = [b]
    while True:
        if parent[a]== 0:
            break
        a = parent[a]
        a_parent.append(a)

    while True:
        if parent[b] == 0:
            break

        b = parent[b]
        b_parent.append(b) 
        
    answer = 0

    for i in range(len(a_parent)):
        find_flag = False
        for j in range(len(b_parent)):
            if a_parent[i] == b_parent[j]:
                find_flag = True
                answer = a_parent[i]
                break
        if find_flag:
            break

    print(answer)    

    