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


            