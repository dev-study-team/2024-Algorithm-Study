k = int(input())
nums = list(map(int, input().split()))
ans = [[] for _ in range(k)]

def dfs(start, end, level):
    if start == end:
        ans[level].append(nums[start])
        return

    mid = (start + end) // 2
    ans[level].append(nums[mid])

    dfs(start, mid -1, level+1)
    dfs(mid +1, end, level+1)


dfs(0, len(nums)-1, 0)
for elem in ans:
    print(*elem)