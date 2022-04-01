class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class LinkedBinaryTree {
  constructor(node) {
    this.root = node;
  }

  stackPreOrder() {
    let stack = [this.root];
    while (stack.length) {
      let node = stack.pop();
      console.log(node.value);
      if (node.right) {
        stack.push(node.right);
      }
      if (node.left) {
        stack.push(node.left);
      }
    }
  }

  stackInOrder() {
    let stack = [this.root];
    let node = this.root;
    while (true) {
      if (node) {
        stack.push(node);
        node = node.left;
      } else if (stack.length) {
        node = stack.pop();
        console.log(node.value);
        node = node.right;
      } else {
        break;
      }
    }
  }

  stackPostOrder() {
    let stack1 = [this.root];
    let stack2 = [];

    while (stack1.length) {
      let root = stack1.pop();
      stack2.push(root);
      if (root.left) {
        stack1.push(root.left);
      }
      if (root.right) {
        stack1.push(root.right);
      }
    }

    while (stack2.length) {
      let root = stack2.pop();
      console.log(root);
    }
  }

  recurInOrder(root) {
    if (root.left) {
      this.recurInOrder(root.left);
    }
    console.log(root.value);
    if (root.right) {
      this.recurInOrder(root.right);
    }
  }

  recurPreOrder(root) {
    console.log(root.value);
    if (root.left) {
      this.recurPreOrder(root.left);
    }
    if (root.right) {
      this.recurPreOrder(root.right);
    }
  }

  recurPostOrder(root) {
    if (root.left) {
      this.recurPostOrder(root.left);
    }
    if (root.right) {
      this.recurPostOrder(root.right);
    }
    console.log(root.value);
  }
}

const tree = new LinkedBinaryTree(new Node(9));
tree.root.left = new Node(3);
tree.root.right = new Node(8);
tree.root.left.left = new Node(2);
tree.root.left.right = new Node(5);
tree.root.left.right.right = new Node(4);
tree.root.right.right = new Node(7);

// tree.recurPreOrder(tree.root);
tree.stackPreOrder();
// tree.recurInOrder(tree.root);
// tree.recurPostOrder(tree.root);
