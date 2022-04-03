

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self) :
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True


    def find(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word  


N,M = map(int,input().split())
trie = Trie()
cnt=0
for _ in range(N):
    word = input()
    trie.insert(word)
for _ in range(M):
    word = input()
    if trie.find(word):
        cnt+=1
print(cnt)
    
