class Node {
  constructor(value = "") {
    this.value = value;
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
        currentNode.children.set(char, new Node(currentNode.value + char));
      }
      currentNode = currentNode.children.get(char);
    }
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

  autoDFS(node, autoWords) {
    //find autoWords
    if (!node.children.size) {
      autoWords.push(node.value);
      return;
    } else {
      if (!node?.children?.children?.size) {
        autoWords.push(node.value);
      }
      for (let char of node.children) {
        this.autoDFS(node.children.get(char[0]), autoWords);
      }
    }
  }

  autoComplete(string) {
    let currentNode = this.root;
    let autoWords = [];

    for (const char of string) {
      if (!currentNode.children.has(char)) {
        return `${string}... not included`;
      }
      currentNode = currentNode.children.get(char);
    }
    this.autoDFS(currentNode, autoWords);
    return autoWords;
  }
}

let trie = new Trie();
trie.insert("java");
trie.insert("javascript");
trie.insert("javascriptab");
trie.insert("java backend");

console.log(trie.autoComplete("javascript"));
console.log(trie.autoComplete("java"));
