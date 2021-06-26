from collections import deque
from itertools import combinations
import copy

def make_wall(elm,MAP):
    COPY_MAP = copy.deepcopy(MAP)
    for xy in elm:
        x=xy[0]
        y=xy[1]
        COPY_MAP[x][y]=1
    return COPY_MAP

def bfs(COPY_MAP):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    visited=[[False for _ in range(len(COPY_MAP[0]))] for _ in range(len(COPY_MAP))]
    q = deque()
    for i in range(len(COPY_MAP)):
        for j in range(len(COPY_MAP[0])):
            if COPY_MAP[i][j]==2:
                q.append([i,j])
                visited[i][j] = True
    
    while q:
        xy = q.popleft()
        y = xy[0]
        x = xy[1]
        for i in range(4):
            nextY = y + dy[i]
            nextX = x + dx[i]

            if nextX < 0 or nextY <0 or nextY >= len(COPY_MAP) or nextX >=len(COPY_MAP[0]):
                continue

            if COPY_MAP[nextY][nextX] == 0 and not visited[nextY][nextX] :
                COPY_MAP[nextY][nextX] = 2
                q.append([nextY,nextX])
                visited[nextY][nextX] = True

    return count_safety(COPY_MAP)


def count_safety(COPY_MAP):
    cnt=0
    for i in range(len(COPY_MAP)):
        for j in range(len(COPY_MAP[0])):
            if COPY_MAP[i][j] ==0 :
                cnt +=1
    return cnt 
        

if __name__ == "__main__":
    MAP=[]
    empty=[]
    MAX= 0
    N,M = map(int,input().split())
    for _ in range(N):
        MAP.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0 :
                empty.append((i,j))

    for elm in list(combinations(empty,3)):
        MAX = max(MAX,(bfs(make_wall(elm,MAP))))
    
    print(MAX)