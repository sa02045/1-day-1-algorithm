from operator import le


if __name__ == "__main__":
    K,N = map(int,input().split())
    lanlines = []
    maxLine = 0
    for _ in range(K):
        line = int(input())
        if maxLine < line :
            maxLine = line
        lanlines.append(line)

    lanlines.sort()
        
    def binarySearch():
        left = 0
        right = maxLine
        while left < right:
            mid = (left + right) // 2
            lanline_sum = 0
            for line in lanlines:
                lanline_sum += line // mid
            if lanline_sum >= N:
                left = mid + 1
            else:
                right = mid
        return right
    print(binarySearch())     
