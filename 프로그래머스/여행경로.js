function solution(tickets) {
  let answer = [];
  let visitedTicket = new Array(tickets.length).fill(false);
  dfs("ICN", ["ICN"]);

  return answer.sort()[0];

  function dfs(currentCity, path) {
    if (path.length === tickets.length + 1) {
      answer.push(path);
      return;
    }

    tickets.forEach(([start, end], idx) => {
      if (visitedTicket[idx]) {
        return;
      }

      if (start === currentCity) {
        visitedTicket[idx] = true;
        dfs(end, [...path, end]);
        visitedTicket[idx] = false;
      }
    });
  }
}
