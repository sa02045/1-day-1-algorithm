let arr = Array.from({ length: 100 }, (v, i) => i + 1); // 1~100

// console.log(recursiveBinarySearch(1, arr.length - 1, arr, 50, 1));
console.log(LowerBound(arr, 50));
// 1. 재귀로 구현
function recursiveBinarySearch(left, right, arr, target, cnt) {
  let mid = Math.floor((left + right) / 2);
  if (arr[mid] === target) {
    return cnt;
  }
  if (target < arr[mid]) {
    return recursiveBinarySearch(left, mid - 1, arr, target, cnt + 1);
  }

  if (target > arr[mid]) {
    return recursiveBinarySearch(mid + 1, right, arr, target, cnt + 1);
  }
}

// 2. loewrBound로 구현 (right=mid)
function LowerBound(arr, target) {
  let left = 0;
  let right = arr.length - 1;
  let cnt = 0;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (target <= arr[mid]) {
      right = mid;
    } else if (target > arr[mid]) {
      left = mid + 1;
    }
    cnt++;
  }
  return cnt;
}
