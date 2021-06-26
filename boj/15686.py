from itertools import combinations
import copy
from collections import deque

def make_new_MAP(elm):
    COPY_MAP= copy.deepcopy(MAP)
    for ij in enumerate(elm):
        i= ij[0]
        j= ij[1]
        COPY_MAP[i][j]=0
    return COPY_MAP

def find_chicken_distance(i,j,COPY_MAP):
    q = deque()
    visited= [[False for in range(N)] for in range(N)]
    q.append([i,j,0])
    visited[i][j]=True
    dx =[-1,0,1,0]
    dy =[0,-1,0,1]

    while q:
        yx = q.popleft()
        y = yx[0]
        x = yx[1]
        cnt = yx[2]

        for i in range(4):
            nextX = dx[i]+x
            nextY = dy[i]+y

            if nextX < 0 or nextY < 0 or nextX >=N or nextY >=N or visited[nextY][nextX]:
                continue

            if COPY_MAP[nextY][nextX]==2:
                return cnt

            q.append([nextY,nextX,cnt+1])

if __name__ =="__main__":
    # 0.빈칸 1.집 2.치킨집
    N,M = map(int,input().split())
    MAP=[]
    chicken_cnt=0
    chicken_list=[]
    for _ in range(N):
        MAP.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N):
            if MAP[i][j]==2:
                chicken_cnt+=1
                chicken_list.append([i,j])

    CHICKEN_DISTANCE=13
    for elm in list(combinations(chicken_list,chicken_cnt-M)):
        CHICKEN_DISTANCE = min(CHICKEN_DISTANCE,bfs(make_new_MAP(elm)))
    

    print(CHICKEN_DISTANCE)