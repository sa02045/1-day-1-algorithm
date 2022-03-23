class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  find(data) {
    let curNode = this.head;

    while (curNode !== null && curNode.data !== data) {
      curNode = curNode.next;
    }

    return curNode;
  }

  append(newdata) {
    const newNode = new Node(newdata);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  insert(node, newdata) {
    const newNode = new Node(newdata);
    newNode.next = node.next;
    node.next = newNode;
  }

  remove(data) {
    let preNode = this.head;
    while (preNode !== null && preNode.next.data !== data) {
      preNode = preNode.next;
    }
    if (preNode.next !== null) {
      preNode.next = preNode.next.next;
    }
  }

  size() {
    let curNode = this.head;
    let size = 0;
    while (curNode !== null) {
      curNode = curNode.next;
      size++;
    }
    return size;
  }
}
