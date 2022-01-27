// 에라토스테네스의 체
//  범위내의 모든 소수를 찾을 때 빠르다

function solution(n) {
  let arr = new Array(n + 1).fill(false);

  // 2부터 n^1/2까지 찾는다 ex) n=9라면 2,3까지
  for (let i = 2; i * i <= n; i++) {
    // 자신은 제외하고 배수부터 지운다 ex) 3은 제외 3+3부터 지운다
    for (let j = i + i; j <= n; j += i) {
      //   배수는 true로 표시
      arr[j] = true;
    }
  }

  let cnt = 0;

  // false라면 소수
  for (let i = 2; i <= n; i++) {
    if (arr[i] === false) {
      cnt += 1;
    }
  }
  return cnt;
}
