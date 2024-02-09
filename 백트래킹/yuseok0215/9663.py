n = int(input())

arr =[] # 1,1 0,2 0,0

def check(arr):
    for i in range(1,len(arr)):
        if arr[i-1][0] == arr[i][0] or arr[i-1][1] == arr[i][1]:
            return False
        elif abs(arr[i-1][0]-arr[i][0]) == 1 or abs(arr[i-1][1]-arr[i][1]) == 1:
            return False
    
    return True
    

def backtracking(depth, arr):
    global cnt

    if depth == n:
        cnt += 1
        return

    for i in range(n):
        for j in range(n):
            arr.append((i,j))
            if check(arr):
                backtracking(depth+1, arr)
            arr.pop()

cnt = 0
backtracking(0, arr)

print(cnt)
