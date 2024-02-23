import sys
input=sys.stdin.readline
from collections import defaultdict

while True:

    n,k = map(int,input().split())
    if [n,k]==[0,0]:
        break

    nums = list(map(int,input().split()))
    parent = defaultdict(int) # 딕셔너리 초기화

    index=0
    for i in range(1,n):
        parent[nums[i]] = nums[index] # 현재 노드의 부모노드를 담는다.
        if i < n-1 and nums[i]+1 < nums[i+1]:
            index+=1

    count=0
    if parent[parent[k]]: # 부모의 부모가 존재한다면
        for num in nums:
            if (parent[parent[k]] == parent[parent[num]]) and parent[num]!=parent[k]: 
                #부모의 부모가 같고 부모가 다르면
                count+=1
    print(count)