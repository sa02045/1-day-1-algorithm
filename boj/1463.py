N=int(input())

dp=[0 for i in range(N+1)]


def sol(x):
    if x == 1:
        return 0
    if x < 4 :
        return 1
    dp[1]=0
    dp[2]=1
    dp[3]=1
    for i in range(3,x+1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i//2],dp[i//3],dp[i-1])+1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3],dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2],dp[i-1]) + 1
        else:
            dp[i] =dp[i-1] +1

    return dp[x]

print(sol(N))