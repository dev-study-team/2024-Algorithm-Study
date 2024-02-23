t = int(input())

for _ in range(t):
    m = int(input())

    num = []
    if m > 10:
        for _ in range(m//10+1):
            tmp = list(map(int, input().split()))
            for elem in tmp:
                num.append(elem)
    else: 
        num = list(map(int, input().split()))

    arr = []
    answer = []
    for i in range(m):
        arr.append(num[i])
        if i % 2 == 0:
            arr.sort()
            answer.append(arr[i//2])
    
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')

        if i % 10 == 9:
            print()

    print()


# heapq

from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


def get_median() -> None:
    left, right, ans = [], [], [nums[0]]
    mid = nums[0]

    for i, num in enumerate(nums[1:], 1):
        if num < mid:
            heappush(left, -num)
        else:
            heappush(right, num)

        if i % 2 == 0:
            if len(left) > len(right):
                heappush(right, mid)
                mid = -heappop(left)
            elif len(left) < len(right):
                heappush(left, -mid)
                mid = heappop(right)
            ans.append(mid)

    print(M // 2 + 1)
    for i, num in enumerate(ans):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M = int(input())
        nums = []
        for _ in range(M // 10 + 1):
            nums += list(map(int, input().split()))

        get_median()
            