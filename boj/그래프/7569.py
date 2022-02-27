from collections import deque
import sys
if __name__ == "__main__":
    M,N,H= map(int,sys.stdin.readline().split())
    MAP=[]

    def isSearchable(h,n,m):
        if h < 0 or n < 0 or m < 0 or h >= H or n >= N or m >= M:
            return False
        if MAP[h][n][m] != 0:
            return False
        return True


    deq = deque()
    def bfs():
        dist = [[0,-1,0],[0,1,0],[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]]
        while deq:
            [prevH,prevN,prevM] = deq.popleft()
            for [offH,offN,offM] in dist:
                nextH,nextN,nextM= prevH+offH,prevN+offN,prevM+offM
                if isSearchable(nextH,nextN,nextM):
                    MAP[nextH][nextN][nextM] = MAP[prevH][prevN][prevM] + 1
                    deq.append([nextH,nextN,nextM])
                
        

    def get_min_day(H,N,M,MAP):
        min_day=-1
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if MAP[h][n][m] == 0:
                        return -1

                    if min_day < MAP[h][n][m] :
                        min_day = MAP[h][n][m]

        return min_day - 1

    for h in range(H):
        MAP.append([])
        for _ in range(N):
            MAP[h].append(list(map(int,sys.stdin.readline().split())))

        
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if MAP[h][n][m] == 1:
                    deq.append([h,n,m])

    bfs()
    print(get_min_day(H,N,M,MAP))