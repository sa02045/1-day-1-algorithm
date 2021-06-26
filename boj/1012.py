import sys
sys.setrecursionlimit(10**5)

T= int(input())

dy = [-1,0,1,0]
dx = [0,-1,0,1]

def dfs(y,x):
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX < 0 or nextY <0 or nextX >= M or nextY >= N or visited[nextY][nextX]==True :
            continue
        if MAP[nextY][nextX]==1:
            visited[nextY][nextX] = True
            dfs(nextY,nextX)

for i in range(T):
    M,N,K = map(int,input().split())
    MAP=[ [0] * M for _ in range(N)]
    visited = [ [False ]* M for _ in range(N)]
    cnt =0
    for _ in range(K):
        X,Y=map(int,input().split())
        MAP[Y][X] = 1

    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                cnt+=1
                dfs(y,x)
    print(cnt)