from unicodedata import name


import heapq
from collections import defaultdict
if __name__ == "__main__":
    graph = defaultdict(list)
    V,E=map(int,input().split())
    K= int(input())
    for i in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))

    Q = [(0,K)]

    dist = defaultdict(int)

    while Q:
        w, v = heapq.heappop(Q)
        if not v in dist:
            dist[v] = w
            for next_w , next_v in graph[v]:
                heapq.heappush(Q,(w+next_w,next_v))

    for v in range(1,V+1):
        if not v in dist:
            print("INF")
        else:
            print(dist[v])


