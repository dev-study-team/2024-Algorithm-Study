# from itertools import combinations
# import sys

# input = sys.stdin.readline
# n,m = map(int, input().split())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))

# # temp = []
# # _min = 1e9
# # def backtracking(temp):
# #     global _min

# #     if len(temp) == 2:
# #         if abs(temp[0]-temp[1]) >= m:
# #             _min = min(_min, abs(temp[0]-temp[1]))

# #     for i in range(n):
# #         if nums[i] not in temp:
# #             temp.append(nums[i])
# #             backtracking(temp)
# #             temp.pop()
        
# # backtracking(temp)

# # print(_min)



# # nums_list = list(combinations(nums, 2))

# # _min = 1e9
# # for a,b in nums_list:
# #     if abs(a-b) >= m:
# #         _min = min(abs(a-b), _min)

# # print(_min)
times = [4,5,6]

table = [0 for _ in range(len(times))]
print(table)