function solution(n, info) {
  dfs(0, info, new Array(11).fill(0), n);
}

function dfs(idx, apeechInfo, lionInfo, n) {
  if (idx === 11) {
    console.log(lionInfo);
    return;
  }
  if (n >= apeechInfo[idx] + 1) {
    lionInfo[idx] = apeechInfo[idx] + 1;
    dfs(idx + 1, apeechInfo, lionInfo, n - (apeechInfo[idx] + 1));
  }
  lionInfo[idx] = 0;
  dfs(idx + 1, apeechInfo, lionInfo, n);
}

solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]);
