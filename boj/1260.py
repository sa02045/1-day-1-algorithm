from collections import deque

if __name__ == "__main__":
    N,M,V= map(int,input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited_dfs = [False]*(N+1)
    visited_bfs = [False]*(N+1)
    for _ in range(M):
        E1,E2 = map(int,input().split())
        graph[E1][E2] = 1
        graph[E2][E1] = 1

    
    def dfs(v):
        visited_dfs[v] = True
        print(v,end=" ")
        for next in range(1,len(graph[v])):
            if graph[v][next] and not visited_dfs[next]:
                dfs(next)

    def bfs(v):
        queue = deque([])
        queue.append(v)
        visited_bfs[v] = True

        while len(queue):
            _v = queue.popleft()
            print(_v,end=" ")
            for next in range(1,len(graph[_v])):
                if graph[_v][next] and not visited_bfs[next]:
                    visited_bfs[next] = True
                    queue.append(next)

    dfs(V)
    print()
    bfs(V)