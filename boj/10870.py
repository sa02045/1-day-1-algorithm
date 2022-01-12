n=int(input())
dp=[0 for i in range(21)]
dp[1]=1
dp[2]=1
def fibo(n):
    if n < 2:
        return n
  
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibo(n))

# 다이나믹 프로그래밍으로 구현
