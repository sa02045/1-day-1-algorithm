from collections import deque

def clean(y,x):
    visited[y][x] = True

def bfs(i,j,d):
    q = deque()

def is_nomore_work(y,x):
    dx=[-1,0,1,0]
    dy=[0,1,-1,0]

    check=False
    for i in range(4):
        nextY = y+dy[i]
        nextX = x+dx[i]

        if visited[nextY][nextX] == True:
            check=True
            break
        

    return check

if __name__ =="__main__":
    N,M = map(int,input().split())
    r,c,d = map(int,input().split())
    MAP=[]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        MAP.append(list(map(int,input().split())))

    cur_y=c
    cur_x=r

    while is_nomore_work():

    bfs(r,c,d)
    print(MAP)