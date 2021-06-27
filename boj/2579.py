if __name__ == "__main__":
    N=int(input())
    step=[0]*(300)
    dp=[0]*(300)
    for i in range(N):
        step[i] = int(input())

    dp[0]=step[0]
    dp[1]=step[0]+step[1]
    dp[2]=max(step[0]+step[2],step[1]+step[2])

    if N <=2:
        print(dp[N-1])

    else :
        for i in range(3,N):
            dp[i] = max(step[i]+dp[i-2],step[i]+step[i-1]+dp[i-3])
        
        print(dp[N-1])
