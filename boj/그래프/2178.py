from collections import deque
if __name__ == "__main__":
    N,M = map(int,input().split())
    
    graph=[]
    visited = [ [0 for _ in range(M)] for _ in range(N) ]
    visited[0][0] = 1

    for i in range(N):
        graph.append(list(map(int,input())))
    
    def bfs():
        dists = [[-1,0],[1,0],[0,1],[0,-1]]
        queue = deque([[0,0]])
        while queue:
            [i,j] = queue.popleft()
            for dist in dists:
                nextI = i + dist[0]
                nextJ = j + dist[1]
                if nextI < 0 or nextJ < 0 or nextI >= N or nextJ >= M:
                    continue
                if graph[nextI][nextJ] == 0 or visited[nextI][nextJ] != 0:
                    continue
                visited[nextI][nextJ] = visited[i][j] + 1
                queue.append([nextI,nextJ])
    bfs()
   
    print(visited[N-1][M-1])