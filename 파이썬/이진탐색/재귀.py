arr = [10,20,30,60,80,110,120,150]

def binarySearch(left,right,target):
    mid = (left+right) // 2
    if target > arr[mid]:
        return binarySearch(mid+1,right,target)
    elif target < arr[mid]:
        return binarySearch(left,mid-1,target)
    elif target == arr[mid]:
        return mid

binarySearch(0,len(arr)-1,30)