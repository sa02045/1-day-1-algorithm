def sol(S,li):
    visited=[False]*(len(li))
    global cnt
    cnt =0

    def dfs(sum):
        global cnt
        if sum == S:
            print(visited)
            cnt += 1
            return
        for i in range(len(li)):
            if visited[i]:
                continue
            visited[i]=True
            dfs(sum+li[i])
            visited[i]=False

    for i in range(len(li)):
        visited[i]=True
        dfs(li[i])
        visited[i]=False


    print(cnt)

N,S=map(int,input().split())
li=list(map(int,input().split()))
sol(S,li)