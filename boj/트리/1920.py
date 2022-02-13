if __name__ == "__main__":
    N = map(int,input())
    A = list(map(int,input().split()))
    M = map(int,input())
    numbers = list(map(int,input().split()))

    A.sort()

    def binarySearch(target,left,right):
        if left > right:
            return 0
        mid = (left + right) // 2

        if target < A[mid]:
            return binarySearch(target,left,mid-1)
        if target > A[mid] :
            return binarySearch(target,mid+1,right)
        if target == A[mid]:
            return 1
    for num in numbers:
        print(binarySearch(num,0,len(A)-1))

