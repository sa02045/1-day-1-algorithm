
import math
N=int(input())
INFINITE = math.inf

dp= [INFINITE for i in range(5001)]

def sol(x):
    dp[3]=1
    dp[5]=1
    for i in range(6,x+1):
        dp[i] = min(dp[i-3],dp[i-5])+1

    if dp[x] == INFINITE:
        return -1
    return dp[x]


print(sol(N))


