https://www.acmicpc.net/problem/10866


import sys
count = int(sys.stdin.readline())

arr = []
for i in range(count) :
    findStr = sys.stdin.readline()
    if "push_front" in findStr :
        num = findStr.split()
        arr.insert(0, int(num[1]))
    elif "push_back" in findStr :
        num = findStr.split()
        arr.append(int(num[1]))
    elif "pop_front" in findStr :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr[0])
            del arr[0]
    elif "pop_back" in findStr :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr.pop())
    elif "size" in findStr :
        print(len(arr))
    elif "empty" in findStr :
        if len(arr) == 0 :
            print(1)
        else :
            print(0)
    elif "front" in findStr :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr[0])    
    elif "back" in findStr :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr[-1])
            



