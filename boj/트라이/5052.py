class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word = True

    def find(self,word):
        node=self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                if node.word:
                    return True
            else:
                return False
        return True

if __name__ == "__main__":
    t= int(input())
    for _ in range(t):
        trie = Trie()
        n=int(input())
        is_valid=True
        for _ in range(n):
            phone_number = input()
            if n ==0:
                trie.insert(phone_number)
            else:
                if trie.find(phone_number):
                    is_valid=False
                else:
                    trie.insert(phone_number)
                    
        if is_valid:
            print("YES")
        else:
            print("NO")



            
