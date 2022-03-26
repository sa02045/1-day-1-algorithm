function solution(n, edges) {
  let graph = {};
  let queue = [[1, 0]];
  let table = { 1: 0 };

  // 그래프 정보 입력
  edges.forEach(([start, end]) => {
    start in graph ? graph[start].push(end) : (graph[start] = [end]);
    end in graph ? graph[end].push(start) : (graph[end] = [start]);
  });

  // 그래프 탐색(BFS)
  while (queue.length) {
    const [v, dist] = queue.shift();

    for (let i = 0; i < graph[v].length; i++) {
      if (!(graph[v][i] in table) || table[graph[v][i]] > dist + 1) {
        table[graph[v][i]] = dist + 1;
        queue.push([graph[v][i], dist + 1]);
      }
    }
  }

  // 최대 거리를 구한 후, 갯수 구하기
  const maxDistance = Math.max(...Object.values(table));
  return Object.values(table).filter((dist) => dist === maxDistance).length;
}

// 다른 사람 풀이
function solution(n, edge) {
  // 그래프 생성 및 입력
  const graph = Array.from(Array(n + 1), () => []);
  for (const [src, dest] of edge) {
    graph[src].push(dest);
    graph[dest].push(src);
  }

  const distance = Array(n + 1).fill(0);
  distance[1] = 1;

  // BFS
  const queue = [1];
  while (queue.length > 0) {
    const src = queue.shift(); // shfint()는 O(n)이지만 요소가 적을 경우에는 자바스크립트엔진에서 최적화를 해줌
    for (const dest of graph[src]) {
      if (distance[dest] === 0) {
        queue.push(dest);
        distance[dest] = distance[src] + 1;
      }
    }
  }

  const max = Math.max(...distance);
  return distance.filter((item) => item === max).length;
}

class Queue {
  constructor() {
    this.queue = [];
    this.front = 0;
    this.rear = 0;
  }
  enqueue(value) {
    this.queue[this.rear++] = value;
  }
  dequeue() {
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front += 1;
    return value;
  }

  isEmpty() {
    return this.front === this.rear;
  }
}
