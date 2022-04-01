if __name__ == "__main__":
    N,M = map(int,input().split())
    trees = list(map(int,input().split()))

    def getLeftHeight(trees,cut_height):
        sum = 0
        for height in trees:
            if height > cut_height:
                sum += height - cut_height
        return sum

    left = 1
    right = max(trees)

    while left < right:
        mid = (left+right) //2
        if getLeftHeight(trees,mid) >= M:
            left = mid + 1
        else:
            right = mid

    print(right-1)