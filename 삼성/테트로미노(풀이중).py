
if __name__ ==  "__main__":
    N,M= map(int,input().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int,input().split())))

    tetromino = [ 
        [(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(1,0),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,0),(1,0),(2,0),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(0,1),(1,1),(2,0)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(1,0),(0,1),(1,1),(0,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(1,0),(0,1),(1,1),(2,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,0),(1,1),(1,2)]
    ]
    MAX = 0
    for i in range(N):
        for j in range(M):
            sum = 0
            for tet in tetromino:
                check=False
                for k in range(4):
                    nextY = i + tet[k][0]
                    nextX = j + tet[k][1]

                    if nextY >= N or nextX >= M:
                        check=True
                        break

                    if check==False:
                        sum += MAP[nextY][nextX]

            MAX = max(sum,MAX)
                
    print(MAX)


    