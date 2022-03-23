from cmath import inf
from collections import deque

if __name__ == "__main__":
    N= int(input())
    dp = [[inf] * (1 << N) for _ in range(N)]
    graph = []

    for i in range(N):
        graph.append(list(map(int,input().split())))

    def dfs(v,visited):
        # 이미 방문한 적이 있다면
        if dp[v][visited] != inf:
            return dp[v][visited]

        # 최종 
        if visited == (1 << N) -1:
            if graph[v][0]:
                return graph[v][0]
            return inf

        for i in range(1,N):
            if not graph[v][i]:
                continue
            if visited & (1 << (i-1)):
                continue
            dp[v][visited] = min(dp[v][visited], graph[v][i]+dfs(i,visited|(1 << (i-1))))
        return dp[v][visited]

    print(dfs(0,1))