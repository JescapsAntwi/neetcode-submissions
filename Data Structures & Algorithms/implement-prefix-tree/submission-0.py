

class TrieNode:
    def __init__(self):
        self.children = {} #character : the node we go down to when visiting that character 
        self.isEndOfWord = False 


class PrefixTree:
    def __init__(self):
        self.root = TrieNode() # initializing trie with root node 
        

    def insert(self, word: str) -> None:
        #start from root node (character)
        node = self.root 

        for ch in word: # go through every character in our word
            if ch not in node.children: # if a character isn't a child
                node.children[ch] = TrieNode() # create a new prefixtree and it to the children
            node = node.children[ch] # move to the child node 
        node.isEndOfWord = True # mark the end of the word to indicate that we have reached the end 


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False 
            node = node.children[ch]
        return node.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for ch in prefix:
            if ch not in node.children:
                return False 
            node = node.children[ch]
        return True
        
        