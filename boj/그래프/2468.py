if __name__ == "__main__":
    N=int(input())
    MAP=[]
    MAX_CNT = 1
    for _ in range(N):
        MAP.append(list(map(int,input().split())))
    
    def is_searchable(i,j,MAP,height):
        if 0<=i<N and 0<=j<N and MAP[i][j] > height:
            return True
        return False

    def dfs(i,j,MAP,visited,height):
        if not is_searchable(i,j,MAP,height):
            return
        if visited[i][j] !=0:
            return
        visited[i][j] = 1
        for [offI,offJ] in [[-1,0],[1,0],[0,1],[0,-1]]:
            nextI,nextJ = i+offI,j+offJ
            dfs(nextI,nextJ,MAP,visited,height)


    for height in range(1,101):
        cnt=0
        is_end = True
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if MAP[i][j] > height and visited[i][j] ==0:
                    is_end = False
                    dfs(i,j,MAP,visited,height)
                    cnt=cnt+1

        if is_end :
            break

        if MAX_CNT < cnt :
            MAX_CNT =cnt

    print(MAX_CNT)

    