t = int(input())

arr = []
for _ in range(t):
    arr.append(input())


for i in arr:
    cnt = 0 # 열린 괄호 개수

    for elem in i:
        if elem == '(':
            cnt += 1
        elif elem == ')':
            cnt -= 1
        
        if cnt < 0:
            print('NO')
            break

    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')