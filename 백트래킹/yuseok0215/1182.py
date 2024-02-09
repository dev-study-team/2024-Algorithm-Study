from itertools import combinations

n,s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for i in range(1,n+1):
    temp = combinations(nums, i)
    for elem in temp:
        if sum(elem) == s:
            cnt += 1

print(cnt)

# 다른풀이
# import sys
# input = sys.stdin.readline
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0

# def subset_sum(idx, sub_sum):
#     global cnt

#     if idx >= n:
#         return

#     sub_sum += arr[idx]

#     if sub_sum == s:
#         cnt += 1
    
#     # 현재 arr[idx]를 선택한 경우의 가지
#     subset_sum(idx+1, sub_sum)

#     # 현재 arr[idx]를 선택하지 않은 경우의 가지
#     subset_sum(idx+1, sub_sum - arr[idx])

# subset_sum(0, 0)
# print(cnt)