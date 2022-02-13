if __name__ == "__main__":
    def lower(target):
        left = 0
        right = len(cards)
        while left < right :
            mid = (left + right) // 2
            if cards[mid] >= target:
                right = mid
            else :
                left = mid + 1
        return right

    def upper(target):
        left = 0
        right = len(cards)
        while left < right :
            mid = (left + right) // 2
            if cards[mid] > target :
                right = mid
            else :
                left = mid + 1
        return right


    N = int(input())
    cards = list(map(int,input().split()))
    M = int(input())
    numbers = list(map(int,input().split()))
    cards.sort()

    for number in numbers:
        print(upper(number)-lower(number),end=" ")