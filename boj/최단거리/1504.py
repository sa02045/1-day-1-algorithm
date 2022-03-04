from cmath import inf
from collections import defaultdict


import heapq
if __name__ == "__main__":
    N,E = map(int,input().split())
    graph = defaultdict(list)
    
    for _ in range(E):
        a,b,c, = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
    v1,v2 = map(int,input().split())


    def get_min_dist(start,end,graph):
        dist = [inf for _ in range(N+1)]
        dist[start] = 0
        Q=[(0,start)]

        while Q:
            w,v = heapq.heappop(Q)
            for next_w,next_v in graph[v]:
                if dist[next_v] > w + next_w:
                    dist[next_v] = w + next_w
                    heapq.heappush(Q,(w + next_w , next_v))
        return dist[end]

    min_dist = min(get_min_dist(1,v2,graph) + get_min_dist(v2,v1,graph) + get_min_dist(v1,N,graph),
        get_min_dist(1,v1,graph) + get_min_dist(v1,v2,graph) + get_min_dist(v2,N,graph))

    print(min_dist if min_dist != inf else -1)