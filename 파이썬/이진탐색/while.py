arr = [10,20,30,60,80,110,120,150]


def binarySearch(target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid -1
        elif target > arr[mid]:
            left = mid + 1
        elif target == arr[mid]:
            break
    return (left+right) //2 

print(binarySearch(80))
