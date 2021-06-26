if __name__ == "__main__":
    n = int(input())
    dp=[0]*(n+1)
    grape=[0]*(n+1)

    for i in range(1,n+1):
        grape[i]=int(input())
        
    dp[1]=grape[1]
    dp[2]=grape[1]+grape[2]
    for i in range(3,n+1):
        dp[i] = max(grape[i]+grape[i-1] + dp[i-3] , grape[i] + grape[i] + dp[i-2])
        dp[i] = max(dp[i-1],dp[i])
    print(dp)
    