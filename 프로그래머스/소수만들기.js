// 조합으로 숫자 세개를 뽑을 수 있는데, 쉽게 3중 for문을 돌렸다
// Math.sqrt(n)으로 루트 n을 만들 수 있다

function solution(nums) {
  let cnt = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (isPrime(nums[i] + nums[j] + nums[k])) {
          cnt++;
        }
      }
    }
  }
  return cnt;
}

function isPrime(num) {
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}
