def DFS(S, V, arr):
    visited = [0] * V+1
    stack = []
    visited[S] = 1
    v = S
    global answer

    while True:
        for w in arr[v]:
            if w == G:
                answer = 1
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접리스트 input 받는 대로 바로 집아넣기 
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        A,B = map(int, input().split())
        arr[A].append(B)
        # print(arr)
    S, G = map(int, input().split())

    answer = 0

    

    print(f'#{tc} {DFS(S,V,arr)}')