// 배열로 구현
const BinaryTree = [null, 9, 3, 8, 2, 5, null, 7, null, null, null, 4];

function PreOrder(rootIdx) {
  console.log(ArrayBinaryTree[rootIdx]);
  if (ArrayBinaryTree[rootIdx * 2]) {
    PreOrder(rootIdx * 2);
  }

  if (ArrayBinaryTree[rootIdx * 2 + 1]) {
    PreOrder(rootIdx * 2 + 1);
  }
}

function InOrder(rootIdx) {
  if (ArrayBinaryTree[rootIdx * 2]) {
    InOrder(rootIdx * 2);
  }
  console.log(ArrayBinaryTree[rootIdx]);

  if (ArrayBinaryTree[rootIdx * 2 + 1]) {
    InOrder(rootIdx * 2 + 1);
  }
}

function PostOrder(rootIdx) {
  if (ArrayBinaryTree[rootIdx * 2]) {
    PostOrder(rootIdx * 2);
  }

  if (ArrayBinaryTree[rootIdx * 2 + 1]) {
    PostOrder(rootIdx * 2 + 1);
  }
  console.log(ArrayBinaryTree[rootIdx]);
}

PostOrder(1);
