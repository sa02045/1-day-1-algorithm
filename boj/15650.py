def dfs(cnt):
    if cnt == M:
        for num in print_list:
            print(num,end=" ")
        
        print("")
        return
    
    for i in range(1,N+1):
        if visited[i]:
            continue

        if print_list[cnt-1] < i:
            print_list.append(i)
            visited[i]=True

            dfs(cnt+1)

            print_list.pop()
            visited[i]=False


        


if __name__ =="__main__":
    N,M=map(int,input().split())

    visited= [False]*(N+1)
    print_list=[]
    for i in range(1,N+1):
        print_list.append(i)
        visited[i]=True
        dfs(1)

        visited[i]=False
        print_list.pop()