class Queue {
  constructor() {
    this.queue = [];
    this.front = 0;
    this.rear = 0;
  }

  enqueue(data) {
    this.queue[this.rear++] = data;
  }

  dequeue() {
    const data = this.queue[this.front];
    delete this.queue[this.front];
    this.front++;
    return data;
  }

  size() {
    return this.rear - this.front;
  }

  peekFront() {
    return this.queue[this.front];
  }

  peekRear() {
    return this.queue[this.rear - 1];
  }

  isEmpty() {
    return this.rear === 0;
  }
}
