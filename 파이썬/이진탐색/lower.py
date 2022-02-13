arr = [10,20,30,30,30,30,60,80,110,120,150]


def binarySearch(target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            right = mid 
        elif target > arr[mid]:
            left = mid + 1
    return right

print(binarySearch(25))
