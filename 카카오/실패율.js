function solution(N, stages) {
  return new Array(N)
    .fill(0)
    .map((val, idx) => {
      const currentStage = idx + 1;
      let failed = stages.filter((stage) => stage === currentStage).length;
      // 아직 클리어하지 못한 플레이어 수
      let total = stages.filter((stage) => stage >= currentStage).length;
      // 스테이지에 도달한 total 플레이어 수
      return [idx + 1, failed / total];
    })
    .sort((a, b) => b[1] - a[1])
    .map((val) => val[0]);
}
