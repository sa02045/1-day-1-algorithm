if __name__ == "__main__":
    N = int(input())

    red_list=[]
    green_list=[]
    blue_list=[]

    dp = [ [0 for _ in range(3)] for _ in range(N)]
    for i in range(N):
        red,green,blue =map(int,input().split())
        red_list.append(red)
        green_list.append(green)
        blue_list.append(blue)
    
    dp[0][0] = red_list[0]
    dp[0][1] = green_list[0]
    dp[0][2] = blue_list[0]

    for i in range(1,N):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + red_list[i]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + green_list[i]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + blue_list[i]

    print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))