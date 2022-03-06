from cmath import inf

if __name__ == "__main__":
    N=int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                graph[i][j] = inf
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])

    for i in range(N):
        for j in range(N):
            if graph[i][j] == inf:
                print(0,end=" ")
            else:
                print(1,end=" ")

        print()