def dfs(cnt):
    if cnt ==M:
        for num in print_list:
            print(num,end=" ")
        
        print("")
        return

    for i in range(1,N+1):
        if visited[i] :
            continue

        visited[i]=True
        print_list.append(i)

        dfs(cnt+1)

        visited[i]=False
        print_list.pop()
    

if __name__ =="__main__":
    N,M = map(int,input().split())
    
    visited = [False]*(N+1)
    print_list=[]
    dfs(0)
