N=int(input())
li=[]
visited = [False]*N
for index in range(N):
    li.append([index,list(map(int,input().split()))])

li=sorted(li,key = lambda x:(x[1][1],x[0]),reverse=True)
answer = 0 
for index_value in li:
    index , time , money = index_value[0] ,index_value[1][0] , index_value[1][1]

    if index + time > N:
        continue

    check = False
    for i in range(index,index+time):
        if visited[i]==True:
            check=True
            break

    if check==False :
        answer += money
        for i in range(index,index+time):
            visited[i]=True
print(answer)

           


    
