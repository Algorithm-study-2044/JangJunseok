# 1차시도. 258ms. 37.25% beats. 엥..그냥 브루트포스 해도 되네.

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = sentence.split()

        for i in range(len(arr)):
            for dic1 in dictionary:
                word = arr[i]
                if word.startswith(dic1):
                    arr[i] = dic1
            
        return " ".join(arr)
    

# 다른 사람의 풀이 참고. 각 word가지고 트리를 만들었다.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char not in node.children:
                return word
            prefix += char
            if node.children[char].isEnd:
                return prefix
            node = node.children[char]
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        result = []
        for word in sentence.split():
            result.append(trie.search(word))
        
        return ' '.join(result)
