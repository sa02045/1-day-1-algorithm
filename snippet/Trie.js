class Node {
  constructor(value, isWord = false) {
    this.value = value;
    this.isWord = isWord;
    this.children = new Map();
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(string) {
    let currentNode = this.root;
    for (const char of string) {
      if (!currentNode.children.has(char)) {
        currentNode.children.set(
          char,
          new Node((currentNode.value || "") + char, false)
        );
      }
      currentNode = currentNode.children.get(char);
    }

    currentNode.isWord = true;
  }

  has(string) {
    let currentNode = this.root;
    for (const char of string) {
      if (!currentNode.children.has(char)) {
        return false;
      }
      currentNode = currentNode.children.get(char);
    }
    return true;
  }

  height(root) {
    if ([...root.children].length === 0) {
      return 0;
    } else {
      return (
        Math.max(
          ...[...root.children.values()].map((child) => this.height(child))
        ) + 1
      );
    }
  }

  search(string) {
    let currentNode = this.root;
    let words = [];

    for (const char of string) {
      if (!currentNode.children.has(char)) {
        return;
      }
      currentNode = currentNode.children.get(char);
    }

    if (currentNode.isWord) {
      words.push(string);
    }

    this.levelOrder(currentNode, words);
    console.log(words);
  }

  levelOrder(root, words) {
    let height = this.height(root);

    for (let level = 1; level <= height; level++) {
      this.printCurrentLevel(root, level, words);
    }
  }

  printCurrentLevel(root, level, words) {
    if (root === null) {
      return;
    }

    if (level === 0 && root.isWord) {
      words.push(root.value);
    } else {
      [...root.children.values()].forEach((child) => {
        this.printCurrentLevel(child, level - 1, words);
      });
    }
  }
}

const trie = new Trie();

const words = [
  "python",
  "nest",
  "jav",
  "javs",
  "java",
  "java split",
  "java substring",
  "javascript",
  "javascript split",
  "javascript array",
  "javascript replace",
  "javascript substring",
];

words.forEach((word) => trie.insert(word));

trie.search("java");
trie.search("javascript");
